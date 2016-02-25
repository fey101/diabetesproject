import datetime

from django.core.validators import validate_email
from django.db import models
from django.utils import timezone

from rest_framework.serializers import ValidationError


CONTENT_TYPE = (
    ("image/png", "PNG"),
    ("image/jpeg", "JPEG"),
    # ("application/pdf", "PDF"),
    # ("application/vnd.ms-excel", "xls"),
    # ("application/msword", "doc"),
    # ("application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    #     "docx"),
    # ("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    #     "xlsx"),
)


def get_directory(instance, filename):
    """
    Determines the upload_to path for every model inheriting for the
    Attachment abstract class
    """

    return "{}/{}".format(instance.__class__.__name__.lower(), filename)


class Gender(models.Model):
    code = models.CharField(max_length=255),
    display = models.CharField(max_length=10)

    def __str__(self):
        """"Return display as string representation of Gender."""
        return self.display
    # class Meta(object):
    #     ordering = ('code',)


class Valueset(models.Model):
    code = models.CharField(max_length=255),
    display = models.CharField(max_length=10)

    class Meta(object):
        abstract = True

    def __str__(self):
        return self.display


class MaritalStatus(Valueset):
    pass


class CommunicationLanguage(Valueset):
    pass


class ContactType(Valueset):
    pass


class Attachment(models.Model):
    """
    A storage for all the attachment

    Attachments include images(png, jpeg) and documents(pdf, excel, word)
    """
    content_type = models.CharField(max_length=100, choices=CONTENT_TYPE)
    data = models.FileField(upload_to=get_directory)
    title = models.CharField(max_length=255)
    creation_date = models.DateTimeField(default=timezone.now)
    size = models.IntegerField(help_text='The size of the attachment in bytes')

    class Meta(object):
        abstract = True

    def __str__(self):
        return self.title


class Person(models.Model):
    """
    A generic person record.

    Demographics and administrative information about a person independent
    of a specific health-related context
    """

    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    other_names = models.CharField(max_length=120, null=True, blank=True)
    gender = models.ForeignKey(Gender, on_delete=models.PROTECT)
    date_of_birth = models.DateField(verbose_name="Date of birth (YYYY-MM-DD)")
    marital_status = models.ForeignKey(MaritalStatus, on_delete=models.PROTECT)
    communication_language = models.ManyToManyField(
        CommunicationLanguage, through='PersonLanguage')

    # @property
    # def communication_language_set(self):
    #     """Convinience method for aligning communication_language."""
    #     return Person.objects.values("communication_language")

    def get_full_name(self):
        """Return the identifying fullname for this User."""
        return " ".join([self.first_name, self.last_name])

    def validate_dob(self):
        """
        Check date of birth is within expected limits.

        ... that is date of birth is less than today
        and less than 150 years
        """
        if self.date_of_birth:
            max_age = 365 * 300
            delta = datetime.timedelta(days=max_age)
            if self.date_of_birth > timezone.now().date():
                raise ValidationError(
                    {'date_of_birth': ('Date of birth cannot' +
                                       ' be a future date')})

            oldest_person = timezone.now().date() - delta
            if self.date_of_birth < oldest_person:
                raise ValidationError(
                    {'date_of_birth': ('A person cannot be more than ' +
                                       '300 years old.')})

    def clean(self):
        self.validate_dob()
        super(Person, self).clean()

    def save(self, *args, **kwargs):
        self.full_clean(exclude=None)
        super(Person, self).save(*args, **kwargs)

    def __str__(self):
        return self.get_full_name()


class PersonPhoto(Attachment):
    """
    Store images for a person

    A person can have more than one photo but only on can be active
    """
    person = models.ForeignKey(Person, on_delete=models.PROTECT)


class PersonLanguage(models.Model):
    """
    A person can have more than one communication Language
    """
    person = models.ForeignKey(
        Person, on_delete=models.PROTECT,
        related_name="communication_language_set")
    communication_language = models.ForeignKey(
        CommunicationLanguage, on_delete=models.PROTECT,
        related_name="persons_set")


class Contact(models.Model):
    """
    Contact details about a person

    A person can have more than one contact and a contact can be of different
    types. e.g e-mail
    """
    errors = []
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    contact_type = models.ForeignKey(ContactType, on_delete=models.PROTECT)
    contact = models.CharField(max_length=50)
    max_phone_number_len = 12
    min_phone_number_len = 11

    def __str__(self):
        return " ".join([self.person.get_full_name(), self.contact])

    def validate_phone_number_is_a_number(self):
        """
        Validate that it only contains numbers
        """
        error_msg = "Phone number must contain digits only."
        try:
            self.errors.remove(error_msg)
        except ValueError:
            if not self.contact.isdigit() and self.contact_type.code == \
                    "phone_number":
                self.errors.append(error_msg)

    def validate_phone_number_max_length(self):
        """
        Maxlength of a phone number should be 12 characters.
        """
        error_msg = "Phone length must not be longer than 12 characters."
        phone_length = len(str(self.contact))

        try:
            self.errors.remove(error_msg)
        except ValueError:
            if phone_length > self.max_phone_number_len and \
                    self.contact_type.code == "phone_number":
                self.errors.append(error_msg)

    def validate_phone_number_min_length(self):
        """
        Minlength of a phone number should be 11 characters.
        """
        error_msg = "Phone length must be greater than or equal to 11\
                characters."
        phone_length = len(str(self.contact))
        try:
            self.errors.remove(error_msg)
        except ValueError:
            if phone_length < self.min_phone_number_len and \
                    self.contact_type.code == "phone_number":
                    self.errors.append(error_msg)

    def validate_email_address_format(self):
        """
        Email address format should be in the form address@domain.top_level
        eg. email@domain.com
        """
        email_address = self.contact
        if self.contact_type.code == "email":
            try:
                validate_email(email_address)
                return True
            except:
                raise ValidationError("Invalid email address.")

    def raise_errors(self):
        if len(self.errors) > 0:
            errors = self.errors
            self.errors = []
            raise ValidationError(errors)

    def clean(self):
        self.validate_phone_number_is_a_number()
        self.validate_phone_number_max_length()
        self.validate_phone_number_min_length()
        self.validate_email_address_format()
        self.raise_errors()
        super(Contact, self).clean()

    def save(self, *args, **kwargs):
        self.full_clean(exclude=None)
        super(Contact, self).save(*args, **kwargs)


class Medication(models.Model):
    name = models.CharField(max_length=255)
    # Amount administered in one dose
    dose = models.DecimalField(max_digits=10, decimal_places=2)
    # administration frequency per day
    dosage = models.IntegerField()
    description = models.CharField(max_length=255)


class HealthDetails(models.Model):
    person = models.OneToOneField(Person, related_name='person_healthdetails')
    weight = models.DecimalField(max_digits=10, decimal_places=4)
    height = models.DecimalField(max_digits=10, decimal_places=4)
    abdominal_girth = models.DecimalField(max_digits=10, decimal_places=2)
    fasting_glucose = models.DecimalField(max_digits=10, decimal_places=4)
    systole = models.IntegerField()
    diastole = models.IntegerField()
    time_taken = models.DateTimeField(default=timezone.now)
    diabetic = models.BooleanField()
    medication = models.ManyToManyField(
        Medication, related_name='medication_users')

    errors = []

    @property
    def bmi(self):
        return self.weight / ((self.height / 100) ** 2)

    @property
    def blood_pressure(self):
        if self.systole and self.diastole:
            return str(self.systole) + "/" + str(self.diastole)

    def validate_high_pulse(self):
        error_msg = "Pulse cannot be higher than 120"
        try:
            self.errors.remove(error_msg)
        except ValueError:
            if (self.pulse > 120):
                self.errors.append(error_msg)

    def validate_low_pulse(self):
        error_msg = "Pulse value cannot be negative"
        try:
            self.errors.remove(error_msg)
        except ValueError:
            if (self.pulse < 1):
                self.errors.append(error_msg)

    def validate_systolic_bp(self):
        error_msg = "Systole cannot be less than 0 or greater than 300"
        try:
            self.errors.remove(error_msg)
        except ValueError:
            if self.systole and (self.systole < 0 or self.systole > 300):
                self.errors.append(error_msg)

    def validate_diastolic_bp(self):
        error_msg = "Diastole cannot be less than 0 or greater than 250"
        try:
            self.errors.remove(error_msg)
        except ValueError:
            if self.diastole and ((self.diastole < 0) or
               (self.diastole > 250)):
                self.errors.append(error_msg)

    def validate_systolic_diastolic(self):
        error_msg = "Diastolic cannot be greater than systolic reading"
        try:
            self.errors.remove(error_msg)
        except ValueError:
            if self.systole and self.diastole and self.systole < self.diastole:
                self.errors.append(error_msg)

    def validate_small_height(self):
        error_msg = "The height value should be positive"
        try:
            self.errors.remove(error_msg)
        except ValueError:
            if self.height < 1:
                self.errors.append(error_msg)

    def validate_max_height(self):
        error_msg = "The height should not be greater than 300 centimeters"
        try:
            self.errors.remove(error_msg)
        except ValueError:
            if self.height > 300:
                self.errors.append(error_msg)

    def validate_low_weight(self):
        error_msg = "The weight value should be positive"
        try:
            self.errors.remove(error_msg)
        except ValueError:
            if self.weight < 1:
                self.errors.append(error_msg)

    def validate_max_weight(self):
        error_msg = "The weight value should be less than 500 Kilogrammes"
        try:
            self.errors.remove(error_msg)
        except ValueError:
            if self.weight > 500:
                self.errors.append(error_msg)

    def raise_error(self):
        if len(self.errors) > 0:
                errors = self.errors
                self.errors = []
                raise ValidationError(errors)

    def clean(self):
        self.validate_low_pulse()
        self.validate_high_pulse()
        self.validate_diastolic_bp()
        self.validate_systolic_bp()
        self.validate_systolic_diastolic()
        self.validate_small_height()
        self.validate_max_height()
        self.validate_low_weight()
        self.validate_max_weight()
        self.raise_error()
        super(HealthDetails, self).clean()

    def save(self, *args, **kwargs):
        self.full_clean(exclude=None)
        super(HealthDetails, self).save(*args, **kwargs)
