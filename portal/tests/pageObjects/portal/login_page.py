# -*- coding: utf-8 -*-
# Code for Life
#
# Copyright (C) 2016, Ocado Innovation Limited
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ADDITIONAL TERMS – Section 7 GNU General Public Licence
#
# This licence does not grant any right, title or interest in any “Ocado” logos,
# trade names or the trademark “Ocado” or any other trademarks or domain names
# owned by Ocado Innovation Limited or the Ocado group of companies or any other
# distinctive brand features of “Ocado” as may be secured from time to time. You
# must not distribute any modification of this program using the trademark
# “Ocado” or claim any affiliation or association with Ocado or its employees.
#
# You are not authorised to use the name Ocado (or any of its trade names) or
# the names of any author or contributor in advertising or for publicity purposes
# pertaining to the distribution of this program, without the prior written
# authorisation of Ocado.
#
# Any propagation, distribution or conveyance of this program must include this
# copyright notice and these terms. You must not misrepresent the origins of this
# program; modified versions of the program must be marked as such and not
# identified as the original program.
from selenium.webdriver.support.ui import Select

from base_page import BasePage
import play_page
import email_verification_needed_page
from portal.tests.pageObjects.registration.teacher_password_reset_form_page import TeacherPasswordResetFormPage
import teach.dashboard_page_new
import teach.onboarding_organisation_page
import teach.onboarding_classes_page
import teach.onboarding_students_page


class LoginPage(BasePage):
    def __init__(self, browser):
        super(LoginPage, self).__init__(browser)

        assert self.on_correct_page('login_page')

    def login(self, email, password):
        self._login(email, password)

        return teach.dashboard_page_new.TeachDashboardPage(self.browser)

    def login_no_school(self, email, password):
        self._login(email, password)

        return teach.onboarding_organisation_page.OnboardingOrganisationPage(self.browser)

    def login_no_class(self, email, password):
        self._login(email, password)

        return teach.onboarding_classes_page.OnboardingClassesPage(self.browser)

    def login_no_students(self, email, password):
        self._login(email, password)

        return teach.onboarding_students_page.OnboardingStudentsPage(self.browser)

    def login_failure(self, email, password):
        self._login(email, password)
        return self

    def _login(self, email, password):
        self.browser.find_element_by_id('id_login-email').send_keys(email)
        self.browser.find_element_by_id('id_login-password').send_keys(password)
        self.browser.find_element_by_name('login').click()

    def has_login_failed(self):
        if not self.element_exists_by_css('.errorlist'):
            return False

        errors = self.browser.find_element_by_id('form-login-teacher').find_element_by_class_name('errorlist').text
        error = 'Incorrect email address or password'
        return error in errors
