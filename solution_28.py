def group_per_user(group_dictionary):
    user_groups = {}
    
    # Go through group_dictionary
    for group, users in group_dictionary.items():
        # Now go through the users in the group
        for user in users:
            if user not in user_groups:
                user_groups[user] = []
            # Now add the group to the list of
            user_groups[user].append(group)

# groups for this user, creating entry
# in the dictionary if necessary
    return(user_groups)

print(group_per_user({
    "local": ["admin", "userA"],
    "public": ["admin", "userB"],
    "administrator": ["admin"] 
}))