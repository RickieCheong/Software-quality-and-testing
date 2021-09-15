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
        data = field.data
        statement = True # True stating that it's not valid while false means it's valid
        if (data >= 1000 and data <=2599) or (data >= 2620 and data <=2899) or (data >= 2921 and data <=2999) or (data >= 3000 and data <=3999) or (data >= 8000 and data <=8999) or (data >= 4000 and data <=4999) or (data >= 9000 and data <=9999) or (data >= 5000 and data <=5999) or (data >= 6000 and data <=6999) or (data >= 7000 and data <=7999) or (data >= 200 and data <=299) or (data >= 2600 and data <=2619) or (data >= 2900 and data <=2920) or (data >= 800 and data <=999):
            statement = False
        if statement:
            raise ValueError("Invalid Postcode")