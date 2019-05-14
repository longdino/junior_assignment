from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

URL = 'http://127.0.0.1:8000'


class MyBlogTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path=r'C:\Python36\Scripts\geckodriver.exe')

    def tearDown(self):
        self.browser.quit()

    def login(self):
        self.browser.get(URL + '/accounts/login/')
        self.browser.find_element_by_id('id_username').send_keys('hayoung')
        self.browser.find_element_by_id('id_password').send_keys('1020asdf')
        self.browser.find_element_by_id('submit-button').click()

    def newPost(self):
        self.login()
        self.browser.get(URL + '/post/new/')
        self.browser.find_element_by_id('id_title').send_keys('test_Title')
        self.browser.find_element_by_id('id_text').send_keys('This is just the testing.')
        self.browser.find_element_by_id('save-button').click()

        time.sleep(1)

        post = self.browser.find_element_by_class_name('post')
        title = post.find_element_by_tag_name('h2').text
        text = post.find_element_by_tag_name('p').text

        self.assertEqual(title, 'test_Title')
        self.assertEqual(text, 'This is just the testing.')

    def newComment(self):
        self.browser.get(URL + '/post/8/')
        self.browser.find_element_by_id('add_comment').click()
        self.browser.find_element_by_id('id_author').send_keys('test_Author')
        self.browser.find_element_by_id('id_text').send_keys('This is just the test comment.')
        self.browser.find_element_by_id('send_button').click()
        self.browser.find_element_by_id('approve_cmt').click()

        time.sleep(1)

        comment = self.browser.find_element_by_class_name('comment')
        author = comment.find_element_by_tag_name('strong').text
        text = comment.find_element_by_tag_name('p').text

        self.assertEqual(author, 'test_Author')
        self.assertEqual(text, 'This is just the test comment.')

    def deleteComment(self):
        self.login()
        self.browser.get(URL + '/post/8')

        comments = self.browser.find_elements_by_class_name('comment')
        comments[len(comments)-1].find_element_by_tag_name('a').click()
        time.sleep(1)

        new_comments = self.browser.find_elements_by_class_name('comment')

        self.assertTrue(len(comments)-1) == len(new_comments)


if __name__ == "__main__":
    test = MyBlogTest()
    test.setUp()
    # You can comment/uncomment the lines below to test each function
    test.login()
    test.newPost()
    test.newComment()
    test.deleteComment()
    #test.tearDown()
