def register():
    name = input("Ismingizni kiriting: ")
    lastname = input("Familyangizni kiriting: ")

    def save():
        nonlocal name, lastname

        with open(f"{name}_{lastname}_malumot.txt", "w") as file:
            file.write(f"Name: {name}\nLastname: {lastname}\n")
    return save
    
res=register()
print(res())