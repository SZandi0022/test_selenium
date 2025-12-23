from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class DemoQATests:
    """کلاس برای اجرای تمام تست‌های DemoQA در یک اجرا"""

    def __init__(self):
        """راه‌اندازی اولیه"""
        self.setup_driver()
        self.base_url = "https://demoqa.com"

    def setup_driver(self):
        """تنظیمات درایور کروم"""
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        # chrome_options.add_argument("--headless")  # اگر نیاز به حالت headless دارید
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )
        self.wait = WebDriverWait(self.driver, 10)

    def run_all_tests(self):
        """اجرای تمام تست‌ها به ترتیب"""
        print("=" * 50)
        print("شروع تست‌های DemoQA Text Box")
        print("=" * 50)

        # تست 1: بررسی عنوان صفحه
        self.test_1_check_page_title()

        # تست 2: پر کردن فرم با داده‌های اولیه
        self.test_2_fill_form_basic_data()

        # تست 3: اعتبارسنجی فرم با داده‌های فارسی
        self.test_3_validate_form_persian_data()

        print("=" * 50)
        print("تمام تست‌ها تکمیل شدند")
        print("=" * 50)

    def test_1_check_page_title(self):
        """تست 1: بررسی عنوان صفحه"""
        print("\n🔍 تست 1: بررسی عنوان صفحه")

        self.driver.get(f"{self.base_url}/text-box")
        time.sleep(2)

        window_title = self.driver.title
        print(f"📄 عنوان صفحه: {window_title}")

        if "ToolsQA" in window_title:
            print("✅ عنوان صفحه صحیح است")
        else:
            print("❌ عنوان صفحه نادرست است")

    def test_2_fill_form_basic_data(self):
        """تست 2: پر کردن فرم با داده‌های اصلی"""
        print("\n📝 تست 2: پر کردن فرم با داده‌های اصلی")

        # باز کردن صفحه (اگر قبلا باز شده، refresh می‌کند)
        self.driver.get(f"{self.base_url}/text-box")
        time.sleep(2)

        # فیلد نام
        search_field = self.driver.find_element(By.ID, "userName")
        search_field.clear()
        search_field.send_keys("saeid zandi")
        print("✅ فیلد نام پر شد: saeid zandi")
        time.sleep(1)

        # فیلد ایمیل
        search_field1 = self.driver.find_element(By.ID, "userEmail")
        search_field1.clear()
        search_field1.send_keys("example@gmail.com")
        print("✅ فیلد ایمیل پر شد: example@gmail.com")
        time.sleep(1)

        # آدرس فعلی
        search_field2 = self.driver.find_element(By.ID, "currentAddress")
        search_field2.send_keys("Iran-Tehran: niyavaran")
        print("✅ آدرس فعلی پر شد")

        # آدرس دائمی
        search_field3 = self.driver.find_element(By.ID, "permanentAddress")
        search_field3.send_keys("Iran - Iran")
        time.sleep(1)
        search_field3.send_keys(Keys.CONTROL + "a")
        search_field3.send_keys(Keys.BACKSPACE)
        search_field3.send_keys("Iran - Iran")
        print("✅ آدرس دائمی پر شد")

        # ارسال فرم
        button_search = self.driver.find_element(By.ID, "submit")
        button_search.click()
        print("✅ فرم ارسال شد")
        time.sleep(2)

    def test_3_validate_form_persian_data(self):
        """تست 3: اعتبارسنجی با داده‌های فارسی"""
        print("\n🔍 تست 3: اعتبارسنجی فرم با داده‌های فارسی")

        # باز کردن صفحه جدید
        self.driver.get(f"{self.base_url}/text-box")
        time.sleep(2)

        # پر کردن فرم با داده‌های فارسی
        self.driver.find_element(By.ID, "userName").send_keys("علی رضایی")
        self.driver.find_element(By.ID, "userEmail").send_keys("test@example.com")
        self.driver.find_element(By.ID, "currentAddress").send_keys("آدرس تستی فارسی")
        self.driver.find_element(By.ID, "permanentAddress").send_keys("آدرس دائمی فارسی")

        # ارسال فرم
        self.driver.find_element(By.ID, "submit").click()
        time.sleep(2)

        try:
            # انتظار برای نمایش نتیجه
            result_section = self.wait.until(
                EC.presence_of_element_located((By.ID, "output"))
            )
            print("✅ بخش نتایج نمایش داده شد")

            # بررسی نتایج
            name_result = self.driver.find_element(By.ID, "name").text
            email_result = self.driver.find_element(By.ID, "email").text

            print(f"📊 نام نمایش داده شده: {name_result}")
            print(f"📧 ایمیل نمایش داده شده: {email_result}")

            # اعتبارسنجی
            if "علی رضایی" in name_result and "test@example.com" in email_result:
                print("✅ تست موفقیت‌آمیز بود! فرم صحیح ارسال شد.")
            else:
                print("❌ داده‌ها به درستی نمایش داده نشده‌اند")

        except Exception as e:
            print(f"❌ تست با خطا مواجه شد: {e}")
            self.driver.save_screenshot("error_screenshot.png")

    def close_browser(self):
        """بستن مرورگر"""
        print("\n🔄 در حال بستن مرورگر...")
        time.sleep(2)
        self.driver.quit()
        print("✅ مرورگر بسته شد")


# اجرای اصلی
if __name__ == "__main__":
    demoqa_tests = DemoQATests()
    

    try:
        demoqa_tests.run_all_tests()
    except Exception as e:
        print(f"❌ خطا در اجرای تست‌ها: {e}")
        demoqa_tests.driver.save_screenshot("fatal_error.png")
    finally:
        demoqa_tests.close_browser()
