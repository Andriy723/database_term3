from .orders.albom_service import AlbomService
albom_service = AlbomService()
from .orders.country_service import CountryService
country_service = CountryService()
from .orders.country_has_music_service import CountryHasMusicService
country_has_music_service = CountryHasMusicService()
from .orders.creator_service import CreatorService
creator_service = CreatorService()
from .orders.creator_has_music_labels_service import CreatorHasMusicLabelsService
creator_has_music_labels_service = CreatorHasMusicLabelsService()
from .orders.downloading_song_service import DownloadingSongService
downloading_song_service = DownloadingSongService()
from .orders.downloading_song_has_person_profile_service import DownloadingSongHasPersonProfileService
downloading_song_has_person_profile_service = DownloadingSongHasPersonProfileService()
from .orders.follower_service import FollowerService
follower_service = FollowerService()
from .orders.follower_has_creator_service import FollowerHasCreatorService
follower_has_creator_service = FollowerHasCreatorService()
from .orders.janre_service import JanreService
janre_service = JanreService()
from .orders.janre_has_music_service import JanreHasMusicService
janre_has_music_service = JanreHasMusicService()
from .orders.music_service import MusicService
music_service = MusicService()
from .orders.music_labels_service import MusicLabelsService
music_labels_service = MusicLabelsService()
from .orders.person_profile_service import PersonProfileService
person_profile_service = PersonProfileService()
from .orders.playlist_service import PlaylistService
playlist_service = PlaylistService()
