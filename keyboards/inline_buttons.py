from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Start Questionnaire ",
        callback_data="start_questionnaire"
    )
    registration_button = InlineKeyboardButton(
        "Registration ",
        callback_data="fsm_start"
    )
    my_profile_button = InlineKeyboardButton(
        "My Profile ",
        callback_data="my_profile"
    )
    random_profile_button = InlineKeyboardButton(
        "View Profile ",
        callback_data="random_profile"
    )
    reference_menu_button = InlineKeyboardButton(
        "Referral Menu ",
        callback_data="reference_menu"
    )

    markup.add(questionnaire_button)
    markup.add(registration_button)
    markup.add(my_profile_button)
    markup.add(random_profile_button)
    markup.add(reference_menu_button)
    return markup


async def questionnaire_one_keyboard():
    markup = InlineKeyboardMarkup()
    yes_button = InlineKeyboardButton(
        "Yes",
        callback_data="yes_1"
    )
    no_button = InlineKeyboardButton(
        "No",
        callback_data="no_1"
    )
    markup.add(yes_button)
    markup.add(no_button)
    return markup


async def admin_keyboard():
    markup = InlineKeyboardMarkup()
    admin_user_list_button = InlineKeyboardButton(
        "User List",
        callback_data="admin_user_list"
    )
    markup.add(admin_user_list_button)
    return markup


async def like_dislike_keyboard(owner_tg_id):
    markup = InlineKeyboardMarkup()
    user_form_like_button = InlineKeyboardButton(
        "Like ",
        callback_data=f"user_form_like_{owner_tg_id}"
    )
    user_form_dislike_button = InlineKeyboardButton(
        "Dislike ",
        callback_data="random_profile"
    )
    markup.add(user_form_like_button)
    markup.add(user_form_dislike_button)
    return markup


async def edit_delete_form_keyboard():
    markup = InlineKeyboardMarkup()
    edit_form_button = InlineKeyboardButton(
        "Edit ",
        callback_data="fsm_start"
    )
    delete_form_button = InlineKeyboardButton(
        "Delete ",
        callback_data="delete_profile"
    )
    markup.add(edit_form_button)
    markup.add(delete_form_button)
    return markup


async def my_profile_register():
    markup = InlineKeyboardMarkup()
    registration_button = InlineKeyboardButton(
        "Registration ",
        callback_data="fsm_start"
    )
    markup.add(registration_button)
    return markup


async def reference_menu_keyboard():
    markup = InlineKeyboardMarkup()
    reference_link_button = InlineKeyboardButton(
        "Referral Link ",
        callback_data="reference_link"
    )
    reference_list_button = InlineKeyboardButton(
        "Referral List ",
        callback_data="reference_list"
    )
    markup.add(reference_link_button)
    markup.add(reference_list_button)
    return markup