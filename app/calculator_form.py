from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TimeField
from wtforms.validators import DataRequired, ValidationError, Optional

# validation for form inputs
class Calculator_Form(FlaskForm):
    # this variable name needs to match with the input attribute name in the html file
    # you are NOT ALLOWED to change the field type, however, you can add more built-in validators and custom messages
    BatteryPackCapacity = StringField("Battery Pack Capacity", [DataRequired()])
    InitialCharge = StringField("Initial Charge", [DataRequired()])
    FinalCharge = StringField("Final Charge", [DataRequired()])
    StartDate = DateField("Start Date", [DataRequired("Data is missing or format is incorrect")], format='%d/%m/%Y')
    StartTime = TimeField("Start Time", [DataRequired("Data is missing or format is incorrect")], format='%H:%M')
    ChargerConfiguration = StringField("Charger Configuration", [DataRequired()])
    PostCode = StringField("Post Code", [DataRequired()])

    # use validate_ + field_name to activate the flask-wtforms built-in validator
    # this is an example for you
    def validate_BatteryPackCapacity(self, field):
        if field.data is None:
            raise ValidationError('Field data is none')
        elif field.data == '':
            raise ValueError("cannot fetch data")

    # validate initial charge here
    def validate_InitialCharge(self, field):
        # another example of how to compare initial charge with final charge
        # you may modify this part of the code
        try: 
            int(field.data)
        except ValueError:
            raise ValueError("Initial charge data error")
        data = int(field.data)
        if data > int(self.FinalCharge.data) or data < 0 or data > 100:
            raise ValueError("Initial charge data error")

    # validate final charge here
    def validate_FinalCharge(self, field):
        try: 
            int(field.data)
        except ValueError:
            raise ValueError("Final charge data error")
        data = int(field.data)
        if data < int(self.InitialCharge.data) or data < 0 or data > 100:
            raise ValueError("Final charge data error")

    # validate start date here
    def validate_StartDate(self, field):
        pass

    # validate start time here
    def validate_StartTime(self, field):
        """
        temp = str(field.data)
        data = temp.split(":")
        print(data)
        """
        pass

    # validate charger configuration here
    def validate_ChargerConfiguration(self, field):
        try: 
            int(field.data)
        except ValueError:
            raise ValueError("Charger configuration data error")
        data = int(field.data)
        if data > 8 or data < 1:
            raise ValueError("Charger configuration data error")

    # validate postcode here
    def validate_PostCode(self, field):
        try:
            int(field.data)
        except ValueError:
            raise ValueError("Invalid Postcode")
        data = int(field.data)
        statement = True  # True stating that it's not valid while false means it's valid
        if (200 <= data <= 299) or (800 <= data <= 999) or (1000 <= data <= 6797) or (6800 <= data <= 9999):
            statement = False
        if statement:
            raise ValueError("Invalid Postcode")

