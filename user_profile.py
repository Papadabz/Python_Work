def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('daniel', 'roybal',
                             location='loveland',
                             job='line cook',
                             favorite_band='hot mulligan')

print(user_profile)