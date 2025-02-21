from TikTokLive import TikTokLiveClient
from TikTokLive.events import ConnectEvent, CommentEvent, GiftEvent, JoinEvent, LikeEvent, ShareEvent, FollowEvent
from colorama import Fore, Style, init


init(autoreset=True)

id =    input("Nhập ID phòng: ")
client: TikTokLiveClient = TikTokLiveClient(unique_id=id)


@client.on(FollowEvent)
async def on_follow(event: FollowEvent) -> None:
    print(f"{Fore.YELLOW}[{event.user.nickname}]{Style.RESET_ALL} : {Fore.CYAN}Đã theo dõi 🎉{Style.RESET_ALL}")

@client.on(ShareEvent)
async def on_share(event: ShareEvent) -> None:
    print(f"{Fore.YELLOW}[{event.user.nickname}]{Style.RESET_ALL} : {Fore.CYAN}Đã chia sẻ 🎉{Style.RESET_ALL}")

@client.on(ConnectEvent)
async def on_connect(event: ConnectEvent):
    print(f"{Fore.GREEN}✅ Kết nối thành công! {Fore.CYAN}@{event.unique_id} {Fore.YELLOW}(Room ID: {client.room_id}){Style.RESET_ALL}")

@client.on(LikeEvent)
async def on_like(event: LikeEvent):
    print(f"{Fore.YELLOW}[{event.user.nickname}]{Style.RESET_ALL} : {Fore.RED}Đã like ❤️ x {Fore.CYAN}{event.count}{Style.RESET_ALL}")

@client.on(GiftEvent)
async def on_gift(event: GiftEvent) -> None:
    count = event.repeat_count if event.gift.streakable and not event.streaking else 1
    print(f"{Fore.YELLOW}[{event.user.nickname}]{Style.RESET_ALL} : {Fore.MAGENTA}Gửi quà 🎁 {Fore.CYAN}{event.gift.name}{Style.RESET_ALL} x {count}")

@client.on(JoinEvent)
async def on_join(event: JoinEvent) -> None:
    nickname = event.user.nickname or "Người dùng ẩn danh"
    print(f"{Fore.MAGENTA}[{nickname}]{Style.RESET_ALL} : {Fore.CYAN}Tham gia phòng!{Style.RESET_ALL}")

async def on_comment(event: CommentEvent) -> None:
    print(f"{Fore.BLUE}[{event.user.nickname}]{Style.RESET_ALL} : {Fore.GREEN}{event.comment}{Style.RESET_ALL}")

client.add_listener(CommentEvent, on_comment)

if __name__ == '__main__':
    
    client.run()
