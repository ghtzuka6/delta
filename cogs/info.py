import discord, time, datetime, psutil
from discord.ext import commands
from discord.ui import View, Button, Select

global start

class info(commands.Cog):
    def __init__(self, bot: commands.AutoShardedBot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_connect(self):
        global start
        start = time.time()

    @commands.command()
    async def uptime(self, ctx):
        uptime = str(
            datetime.timedelta(seconds=int(round(time.time() - start))))
        e = discord.Embed(
            color=0x2f3136,
            description=f"**{self.bot.user.name}'s** uptime: **{uptime}**")
        await ctx.reply(embed=e, mention_author=False)

    @commands.command()
    async def ping(self, ctx):
        await ctx.reply(f"took `{round(self.bot.latency * 1000)}ms` to ping **a hot asian women**", mention_author=False)

    @commands.command()
    async def botinfo(self, ctx):
        avatar_url = self.bot.user.avatar.url
        uptime = str(
            datetime.timedelta(seconds=int(round(time.time() - start))))
        members = 0
        for guild in self.bot.guilds:
            members += guild.member_count - 1

        embed = discord.Embed(
            color=0x2f3136,
            title=self.bot.user.name,
            description=
            "Multipurpose discord bot...[lol](https://discord.gg/NBDjqe23bH)")
        embed.set_thumbnail(url=f'{avatar_url}')
        embed.add_field(
            name="statistics",
            value="guilds: " + " ** "
            f"{len(self.bot.guilds)}" + "**\nusers: " + f"**{members}" +
            " ** \ndiscord.py version: " + f" **{discord.__version__}**\nping: " +
            f"**{round(self.bot.latency * 1000)}ms**\n" +
            f"uptime: **{uptime}**\nram usage: **{psutil.virtual_memory()[2]}%**"
        )
        await ctx.reply(embed=embed, mention_author=False)

    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(
            color=0x2f3136,
            description="if you want to add me on your server you can click below")
        embed.set_author(name=self.bot.user.name,
                         icon_url=self.bot.user.avatar.url)
        button1 = Button(label="support", url="https://discord.gg/NBDjqe23bH")
        button2 = Button(
            label="invite",
            url=
            "https://discord.com/oauth2/authorize?client_id=1014050243328888894&permissions=8&scope=bot%20applications.commands"
        )
        view = View()
        view.add_item(button1)
        view.add_item(button2)
        await ctx.reply(embed=embed, view=view, mention_author=False)

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(color=0x2f3136, description="")
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        embed.set_author(name="help panel", icon_url=self.bot.user.avatar.url)
        embed.add_field(name="commands",
                        value="use the dropdown menu below to see commands",
                        inline=False)
        embed.add_field(
            name="contact",
            value=
            "if you need support you can contact us in the [support server](https://discord.gg/NBDjqe23bH)"
        )
        button1 = Button(label="support", url="https://discord.gg/NBDjqe23bH")
        button2 = Button(
            label="invite",
            url=
            f"https://discord.com/oauth2/authorize?client_id={self.bot.user.id}&permissions=8&scope=bot%20applications.commands"
        )
        select = Select(
            placeholder="select category",
            options=[
                discord.SelectOption(label="home"),
                discord.SelectOption(label="info"),
                discord.SelectOption(label="utility"),
                discord.SelectOption(label="moderation")
            ])

        async def select_callback(interaction: discord.Interaction):
            if interaction.user != ctx.author:
                em = discord.Embed(
                    color=0xffff00,
                    description=
                    f"<:check_warning:956780930066964500> {interaction.user.mention} you are not the author of this message"
                )
                await interaction.response.send_message(embed=em, ephemeral=True)
                return

            if select.values[0] == "home":
                await interaction.response.edit_message(embed=embed)
            elif select.values[0] == "info":
                e = discord.Embed(color=0x2f3136, title="info commands")
                e.set_thumbnail(url=self.bot.user.avatar.url)
                e.add_field(name="info",
                            value="`botinfo`, `ping`, `uptime`,`userinfo`,`server`",
                            inline=False)
                await interaction.response.edit_message(embed=e)
            elif select.values[0] == "utility":
                e = discord.Embed(color=0x2f3136,
                                  title="utility Commands")
                e.set_thumbnail(url=self.bot.user.avatar.url)
                e.add_field(name="utility",
                            value="`membercount`, `server`, `snipe` `userinfo`, `voicecount`,`banner`,`avatar`",
                            inline=False)
                await interaction.response.edit_message(embed=e)
            elif select.values[0] == "moderation":
                e = discord.Embed(color=0x2f3136, title="moderation commands")
                e.set_thumbnail(url=self.bot.user.avatar.url)
                e.add_field(name="moderation", value="`kick`, `ban`, `unban`, `autoresponder`", inline=False)
                await interaction.response.edit_message(embed=e)

        select.callback = select_callback 

        view = View()
        view.add_item(select)
        view.add_item(button1)
        view.add_item(button2)      

        await ctx.reply(embed=embed, view=view, mention_author=False)  


async def setup(bot) -> None:
    await bot.add_cog(info(bot))
