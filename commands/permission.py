import discord
from discord.ext import commands

from config import bot_color
from config import member_icon
from config import role_icon


class permission(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    permission = discord.SlashCommandGroup("permission", "Manage permissions", hidden=False, guild_only=True, default_member_permissions=discord.Permissions(manage_roles=True))

    @permission.command(name="showmember", description="Show permissions for a member")
    @discord.option("member", discord.Member, description="Select a member", required=True)
    async def show_member_perms(self, ctx, member: discord.Member):
        permissions = ', '.join([str(perm[0]).replace("_", " ") for perm in member.guild_permissions if perm[1]])

        if permissions == "":
            permissions = "*There are no permissions for this member*"

        embed = discord.Embed(color=bot_color, description=permissions)
        embed.set_author(name=f"Permissions for {member.name}", icon_url=member_icon)
        await ctx.respond(embed=embed, ephemeral=True)


    @permission.command(name="showrole", description="Show permissions for a role")
    @discord.option("role", discord.Role, description="Select a role", required=True)
    async def show_role_perms(self, ctx, role: discord.Role):
        permissions = ', '.join([str(perm[0]).replace("_", " ") for perm in role.permissions if perm[1]])

        if permissions == "":
            permissions = "*There are no permission offsets for this role*"

        embed = discord.Embed(color=bot_color, description=permissions)
        embed.set_author(name=f"Permissions for {role.name}", icon_url=role_icon)
        await ctx.respond(embed=embed, ephemeral=True)


def setup(bot: commands.Bot):
    bot.add_cog(permission(bot))
      