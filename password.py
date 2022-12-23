import re
def Store():
    password = "Martin123678MJKIBVRWYmdieh*&"
score = {"strong": 10, "medium": 5, "weak": 5}
# score_list = []
# weakness_list = []

# check the length


class PasswordChecker:
    def __init__(self):
        self.score_list = []
        self.weakness_list = []
    def check_length(self,password):
        passwordLen = len(password)
        if passwordLen <= 4:
            self.score_list.append(score["weak"])
            self.weakness_list.append(f"password len is {passwordLen}")
            # self.checkSpecial(password)
        if passwordLen > 4 and passwordLen <= 7:
            self.score_list.append(score["medium"])
            self.weakness_list.append(f"password len is {passwordLen}")
            self.checkSpecial(password)
        if passwordLen > 8:
            self.score_list.append(score["strong"])
            self.checkSpecial(password)

    # check for special character
    def checkSpecial(self,password):
        special_char = re.compile("[@_!#$%^&*()<>?/\|}{~:]")
        parser = special_char.findall(password)
        if bool(parser) == True:
            if len(parser) < 2:
                self.score_list.append(score["medium"])
                self.weakness_list.append(f"number of special character {parser}")
                self.checkCase(password)
            else:
                self.score_list.append(score["strong"])
                self.checkCase(password)
        else:
            self.score_list.append(score["weak"])
            self.weakness_list.append(f"password lacks special character")
            self.checkCase(password)

    def checknumbers(self,password):
        number_count = 0
        isNumber = False
        for num in password:
            if num.isdigit():
                number_count += 1
                isNumber = True
        if isNumber:
            if number_count < 3:
                self.score_list.append(score["weak"])
            elif number_count > 3 and number_count < 5:
                self.score_list.append(score["medium"])
            elif number_count > 5:
                self.score_list.append(score["strong"])

        else:
            self.weakness_list.append(f"password lacks numbers/digits character")
            self.score_list.append(score["weak"])

    # check case

    def checkCase(self,password):
        
        uppercase = False
        lowercase = False
        upper_count = 0
        lower_count = 0
        number_count = 0
        isNumber = False
        for c in password:
            if c.isupper():
                upper_count += 1
                uppercase = True
            elif c.islower():
                lower_count += 1
                lowercase = True
            elif c.isdigit():
                number_count += 1
                isNumber = True

        case_value = abs(upper_count-lower_count)
        if uppercase and lowercase:
            if case_value > 4:
                self.weakness_list.append(
                    f"mixture of uppecase and lowercase letter is not enough")

                self.score_list.append(score["weak"])
                self.checknumbers(password)
            elif case_value < 4 and upper_count < 2:
                self.weakness_list.append(
                    f"mixture of uppecase and lowercase letters is not enough")
                self.score_list.append(score["mediam"])
                self.checknumbers(password)
            elif case_value < 4 and upper_count > 2:
                self.score_list.append(score["strong"])
                self.checknumbers(password)

        else:
            self.score_list.append(score["weak"])
            self.weakness_list.append(
                f"the password does not contain mixture of uppercase and lowercase letters")

    def input_passwod(self,password):
        self.check_length(password)
        Total_score = 0
        for num in self.score_list:
            Total_score += num
        reports = {}
        percentage = (Total_score/40)*100
        reports['total_score'] = 40
        reports["points_earned"] = Total_score
        reports["weaknesses"] = self.weakness_list
        reports["percentage"] = "{:.2f}%".format(percentage)
        return reports

    