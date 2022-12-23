import re
password = "Martin123678MJKIBVRWYmdieh*&"
score = {"strong": 10, "medium": 5, "weak": 5}
score_list = []
weakness_list = []

# check the length


class PasswordChecker:
    def check_length(password):
        passwordLen = len(password)
        if passwordLen <= 4:
            score_list.append(score["weak"])
            weakness_list.append(f"password len is {passwordLen}")
            PasswordChecker.checkSpecial(password)
        if passwordLen > 4 and passwordLen <= 7:
            score_list.append(score["medium"])
            weakness_list.append(f"password len is {passwordLen}")
            PasswordChecker.checkSpecial(password)
        if passwordLen > 8:
            score_list.append(score["strong"])
            PasswordChecker.checkSpecial(password)

    # check for special character
    def checkSpecial(password):
        special_char = re.compile("[@_!#$%^&*()<>?/\|}{~:]")
        parser = special_char.findall(password)
        if bool(parser) == True:
            if len(parser) < 2:
                score_list.append(score["medium"])
                weakness_list.append(f"number of special character {parser}")
                PasswordChecker.checkCase(password)
            else:
                score_list.append(score["strong"])
                PasswordChecker.checkCase(password)
        else:
            score_list.append(score["weak"])
            weakness_list.append(f"password lacks special character")
            PasswordChecker.checkCase(password)

    def checknumbers(password):
        number_count = 0
        isNumber = False
        for num in password:
            if num.isdigit():
                number_count += 1
                isNumber = True
        if isNumber:
            if number_count < 3:
                score_list.append(score["weak"])
            elif number_count > 3 and number_count < 5:
                score_list.append(score["medium"])
            elif number_count > 5:
                score_list.append(score["strong"])

        else:
            weakness_list.append(f"password lacks numbers/digits character")
            score_list.append(score["weak"])

    # check case

    def checkCase(password):
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
                weakness_list.append(
                    f"mixture of uppecase and lowercase letter is not enough")

                score_list.append(score["weak"])
                PasswordChecker.checknumbers(password)
            elif case_value < 4 and upper_count < 2:
                weakness_list.append(
                    f"mixture of uppecase and lowercase letters is not enough")
                score_list.append(score["mediam"])
                PasswordChecker.checknumbers(password)
            elif case_value < 4 and upper_count > 2:
                score_list.append(score["strong"])
                PasswordChecker.checknumbers(password)

        else:
            score_list.append(score["weak"])
            weakness_list.append(
                f"the password does not contain mixture of uppercase and lowercase letters")

    def input_passwod(password):
        PasswordChecker.check_length(password)
        Total_score = 0
        for num in score_list:
            Total_score += num
        reports = {}
        percentage = (Total_score/40)*100
        reports['total_score'] = 40
        reports["points_earned"] = Total_score
        reports["weaknesses"] = weakness_list
        reports["percentage"] = "{:.2f}%".format(percentage)
        return reports
