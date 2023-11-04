async def discriminator(user: str, discriminator: str):
    return f"{user}#{discriminator}" if discriminator != "0" else user
