from selenium import webdriver
# import allure


def before_scenario(context, driver):
    print('Launh Browser')
    context.driver = webdriver.Chrome(webdriver.ChromeOptions())


def after_scenario(context, drover):
    context.driver.quit()


# def after_step(context, step):
#     if step.status == 'failed':
#         allure.attach(context.driver.get_screenshot_as_png(),
#                       name='screenshot',attachment_type=allure.attachment_type.PNG)