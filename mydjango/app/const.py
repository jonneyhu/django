

class Config:
    CURRENCY='AUD'

from enum import Enum


# users table user role column
class UserRoleType(Enum):
    user = 0
    admin = 1


# user_profiles table KYC_status column
class UserKycType(Enum):
    passed = 0
    failed = 1
    no_submit = 2
    reviewing = 3


# google_verify_types table type_value column
class GoogleType(Enum):
    login = 0
    # reset_password = 1
    withdraw = 2


# id document type
class IdDocumentType(Enum):
    proof_of_age_card = 0
    passport = 1
    australia_driver_license = 2


class FileType(Enum):
    bank_statement = 0
    tax_bill = 1
    utility_bill = 2
    telephone_bill = 3
    rates_notice = 4
    vehicle_registration_certificate = 5
    residential_lease = 6
    council_rates_notice = 7
    contract_of_property_purchase = 8


class DepositOrWithdrawStatus(Enum):
    submitting = 0
    cancelled = 1
    accepted = 2
    pending = 3
    processed = 4
    reject = 5
    done = 6


class NotificationOperate(Enum):
    sign_in = 0
    withdraw = 1
    deposit = 2


class LogType(Enum):
    create = 0
    update = 1
    delete = 2