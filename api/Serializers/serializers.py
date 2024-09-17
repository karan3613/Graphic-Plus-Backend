from typing import List


def user_serializer(user) -> dict:
    return {
        "id": str(user["_id"]),
        "univ_id": user['univ_id'],
        "firstname": user['firstname'],
        "fathername": user['fathername'],
        "mothername": user['mothername'],
        "lastname": user['lastname'],
        "grade12": user["grade12"],
        "grade10": user["grade10"],
        "section": user["section"],
        "rollNo": user['rollNo'],
        "univ_rollNo": user['univ_rollNo'],
        "branch": user['branch'],
        "course": user['course'],
        "image": user['image'],
        "middlename": user['middlename'],
        "dob": user['dob'],
        "email": user['email']
    }


def attendance_serializer(attendance) -> dict:
    return {
        "id": str(attendance['_id']),
        "univ_id": attendance['univ_id'],
        "subjects": attendance['subjects']
    }


def community_serializer(community) -> dict:
    return {
        "id": str(community['_id']),
        "mainVideo": community['mainVideo'],
        "banner": community['banner'],
        "club_name": community['club_name'],
        "club_description": community['club_description'],
        "event_name": community['event_name'],
        "event_description": community['event_description'],
        "qr_image": community['qr_image'],
        "form_link": community['form_link'],
        "social_media_link": community['social_media_link'],
        "extra_link": community['extra_link'],
        "members": community['members'],
        "whatsapp_group": community['whatsapp_group']
    }


def list_communities_serializer(communities) -> list:
    return [community_serializer(community) for community in communities]
