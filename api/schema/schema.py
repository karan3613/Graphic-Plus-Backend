from typing import List
from pydantic import BaseModel


class Login(BaseModel):
    univ_id: str
    password: str


class User(BaseModel):
    univ_id: str
    fathername: str
    mothername: str
    firstname: str
    lastname: str
    grade12: str
    grade10: str
    section: str
    rollno: str
    univ_rollNo: str
    branch: str
    course: str
    image: str
    middlename: str
    dob: str
    email: str


class ForgotPassword(BaseModel):
    univ_id: str
    email: str
    dob: str


class ForgotId(BaseModel):
    mobile_no: str
    dob: str


class Subject(BaseModel):
    subject_name: str
    subject_code: str
    subject_faculty: str
    total_classes: int
    present_classes: int


class Attendance(BaseModel):
    univ_id: str
    subjects: List[Subject]


class Links(BaseModel):
    primary: str
    secondary: str


class Member(BaseModel):
    member_name: str
    contact_info: str


class Community(BaseModel):
    mainVideo: str
    banner: str
    club_name: str
    club_description : str
    event_name : str
    event_description : str
    form_link : str
    social_media_link : str
    secondary_link : str
    qr_image: str
    members: List[Member]
    whatsapp_group: str


class Communities(BaseModel):
    communities: Community
