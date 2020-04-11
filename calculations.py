

def calc_bmr(weight, height, age):
    """
    :param weight: weight in kg
    :param height: height in cm
    :param age: age in years
    :return: bmr
    """
    return 10 * weight + 6.25 * height - 5 * float(age)

def calc_tdee(bmr, rel_exercise, goal):
    """
    :param bmr: base metabolic rate (base = basal?)
    :param rel_exercise: relative amount of exercise per week
    :return: daily caloric goal
    """
    # todo: add bulking multiplers
    if goal == 'cut':
        multiplier_dict = {
            'sedentary': 1.15,
            'light_low': 1.2,
            'light_high': 1.35,
            'moderate_low': 1.4,
            'moderate_high': 1.55,
            'active_low': 1.6,
            'active_high': 1.75,
            'extra_active_low': 1.8,
            'extra_active_high': 1.95
        }

    return bmr * multiplier_dict[rel_exercise]


def lb_to_kg(lb):
    return lb / 2.2


def ft_in_to_cm(height):
    feet, inch = height.split("'")
    return (float(feet)*12 + float(inch)) * 2.54


def calc_cal_by_macro(tdee, goal):
    if goal == 'cut':
        prop_dict = {
            'protein': 0.4,
            'carb': 0.4,
            'fat': 0.2
        }
    # todo: add prop_dict for bulk
    return tdee * prop_dict['protein'], tdee * prop_dict['carb'], tdee * prop_dict['fat']


def calc_g_macro_from_cal_goal(protein_cal, carb_cal, fat_cal):
    cal_per_g_protein = 4
    cal_per_g_carb = 4
    cal_per_g_fat = 9

    return protein_cal/cal_per_g_protein, carb_cal/cal_per_g_carb, fat_cal/cal_per_g_fat


def calc_target_cal(tdee, goal):
    if goal == 'cut':
        return tdee * 0.75
    elif goal == 'bulk':
        return tdee * 1.2
    else:
        return tdee


def main():
    weight = float(input('enter your weight in lbs'))
    weight = lb_to_kg(weight)
    height = input("enter your height in ft, in separated by \"'\" (eg. 6'2)")
    height = ft_in_to_cm(height)
    age = input('enter your age in years')

    bmr = calc_bmr(weight, height, age)
    goal = 'cut'
    activity_level = 'sedentary'
    tdee = calc_tdee(bmr, activity_level, goal) # todo: add an input from drop down later
    protein_cal_goal, carb_cal_goal, fat_cal_goal = calc_cal_by_macro(tdee, 'cut')
    protein_g_goal, carb_g_goal, fat_g_goal = calc_g_macro_from_cal_goal(protein_cal_goal, carb_cal_goal, fat_cal_goal)
    target_calorie = calc_target_cal(tdee, goal)

    print("Your TDEE with a {} lifestyle is {} cal\n".format(activity_level, round(tdee)),
          "TARGETS:\n",
          "Total caloric goal for {}: {} cal\n".format(goal, round(target_calorie)),
          "{} g protein\n".format(round(protein_g_goal, 2)),
          "{} g carb\n".format(round(carb_g_goal, 2)),
          "{} g fat)".format(round(fat_g_goal, 2)))



if __name__ == '__main__':
    main()



