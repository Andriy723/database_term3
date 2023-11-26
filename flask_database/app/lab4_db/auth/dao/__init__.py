from .orders.albom_dao import AlbomDAO
from .orders.country_dao import CountryDAO
from .orders.country_has_music_dao import CountryHasMusicDAO
from .orders.creator_dao import CreatorDAO
from .orders.creator_has_music_labels_dao import CreatorHasMusicLabelsDAO
from .orders.downloading_song_dao import DownloadingSongDAO
from .orders.downloading_song_has_person_profile_dao import DownloadingSongHasPersonProfileDAO
from .orders.follower_dao import FollowerDAO
from .orders.follower_has_creator_dao import FollowerHasCreatorDAO
from .orders.janre_dao import JanreDAO
from .orders.janre_has_music_dao import JanreHasMusicDAO
from .orders.music_dao import MusicDAO
from .orders.music_labels_dao import MusicLabelsDAO
from .orders.person_profile_dao import PersonProfileDAO

albom_dao = AlbomDAO()
country_dao = CountryDAO()
country_has_music_dao = CountryHasMusicDAO()
creator_dao = CreatorDAO()
creator_has_music_labels_dao = CreatorHasMusicLabelsDAO()
downloading_song_dao = DownloadingSongDAO()
downloading_song_has_person_profile_dao = DownloadingSongHasPersonProfileDAO()
follower_dao = FollowerDAO()
follower_has_creator_dao = FollowerHasCreatorDAO()
janre_dao = JanreDAO()
janre_has_music_dao = JanreHasMusicDAO()
music_dao = MusicDAO()
music_labels_dao = MusicLabelsDAO()
person_profile_dao = PersonProfileDAO()
