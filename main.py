import instaloader

L = instaloader.Instaloader()

profile_name = input("Digite o nome do perfil: ")

try:
    profile = instaloader.Profile.from_username(L.context, profile_name)
except intaloader.exceptions.ProfileNoExistsException:
    print("Perfil não encontrado")
    exit()

for post in profile.get_posts():
    L.download_post(post, target=profile.username)