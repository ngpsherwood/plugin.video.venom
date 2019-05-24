# -*- coding: utf-8 -*-

'''
    Venom Add-on
'''

import urlparse,sys,urllib,xbmcaddon,xbmcgui

from resources.lib.modules import control


params = dict(urlparse.parse_qsl(sys.argv[2].replace('?','')))
action = params.get('action')

subid = params.get('subid')
name = params.get('name')
title = params.get('title')
year = params.get('year')
imdb = params.get('imdb')
tvdb = params.get('tvdb')
tmdb = params.get('tmdb')
season = params.get('season')
episode = params.get('episode')
tvshowtitle = params.get('tvshowtitle')
premiered = params.get('premiered')
url = params.get('url')
image = params.get('image')
meta = params.get('meta')
select = params.get('select')
query = params.get('query')
source = params.get('source')
content = params.get('content')

windowedtrailer = params.get('windowedtrailer')
windowedtrailer = int(windowedtrailer) if windowedtrailer in ("0","1") else 0



if action == None:
    from resources.lib.indexers import navigator
    from resources.lib.modules import cache
    run = control.setting('first.info')
    if run == '': run = 'true' #clean install scenerio
    if cache._find_cache_version(): run = 'true'  #check whether plugin.video.venom has been updated-use to be for script.module.venom
    if run == 'true':
        navigator.navigator().news()
        control.setSetting(id='first.info', value='false')
    cache.cache_version_check()
    navigator.navigator().root()



####################################################
#---News
####################################################

elif action == 'newsNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().news()


elif action == 'infoCheck':
    from resources.lib.indexers import navigator
    navigator.navigator().infoCheck('')



####################################################
#---MOVIE
####################################################

elif action == 'movieNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().movies()


elif action == 'movieliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().movies(lite=True)


elif action == 'mymovieNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().mymovies()


elif action == 'mymovieliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().mymovies(lite=True)


elif action == 'movies':
    from resources.lib.indexers import movies
    movies.movies().get(url)


elif action == 'moviePage':
    from resources.lib.indexers import movies
    movies.movies().get(url)


elif action == 'newMovies':
    from resources.lib.indexers import movies
    movies.movies().newMovies()


elif action == 'movieSearch':
    from resources.lib.indexers import movies
    movies.movies().search()


elif action == 'movieSearchnew':
    from resources.lib.indexers import movies
    movies.movies().search_new()


elif action == 'movieSearchterm':
    from resources.lib.indexers import movies
    movies.movies().search_term(name)


elif action == 'moviePerson':
    from resources.lib.indexers import movies
    movies.movies().person()


elif action == 'movieGenres':
    from resources.lib.indexers import movies
    movies.movies().genres()


elif action == 'movieLanguages':
    from resources.lib.indexers import movies
    movies.movies().languages()


elif action == 'movieCertificates':
    from resources.lib.indexers import movies
    movies.movies().certifications()


elif action == 'movieYears':
    from resources.lib.indexers import movies
    movies.movies().years()


elif action == 'moviePersons':
    from resources.lib.indexers import movies
    movies.movies().persons(url)


elif action == 'movieUserlists':
    from resources.lib.indexers import movies
    movies.movies().userlists()



####################################################
#---Collections
####################################################

elif action == 'collectionsNavigator':
    from resources.lib.indexers import collections
    # navigator.navigator().collections()
    collections.collections().collectionsNavigator()

elif action == 'collectionActors':
    from resources.lib.indexers import collections
    collections.collectionsr().collectionActors()


elif action == 'collectionBoxset':
    from resources.lib.indexers import collections
    collections.collections().collectionBoxset()

elif action == 'collectionKids':
    from resources.lib.indexers import collections
    collections.collections().collectionKids()


elif action == 'collectionBoxsetKids':
    from resources.lib.indexers import collections
    collections.collections().collectionBoxsetKids()


elif action == 'collectionSuperhero':
    from resources.lib.indexers import collections
    collections.collections().collectionSuperhero()


elif action == 'collections':
    from resources.lib.indexers import collections
    collections.collections().get(url)



####################################################
#---Furk
####################################################

elif action == "furkNavigator":
    from resources.lib.indexers import navigator
    navigator.navigator().furk()


elif action == "furkMetaSearch":
    from resources.lib.indexers import furk
    furk.furk().furk_meta_search(url)


elif action == "furkSearch":
    from resources.lib.indexers import furk
    furk.furk().search()


elif action == "furkUserFiles":
    from resources.lib.indexers import furk
    furk.furk().user_files()


elif action == "furkSearchNew":
    from resources.lib.indexers import furk
    furk.furk().search_new()



####################################################
# TV Shows
####################################################

elif action == 'tvNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().tvshows()


elif action == 'tvliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().tvshows(lite=True)


elif action == 'mytvNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().mytvshows()


elif action == 'mytvliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().mytvshows(lite=True)


elif action == 'channels':
    from resources.lib.indexers import channels
    channels.channels().get()


elif action == 'tvshows':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().get(url)


elif action == 'tvshowPage':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().get(url)


elif action == 'tvSearch':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().search()


elif action == 'tvSearchnew':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().search_new()


elif action == 'tvSearchterm':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().search_term(name)
    

elif action == 'tvPerson':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().person()


elif action == 'tvGenres':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().genres()


elif action == 'tvNetworks':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().networks()


elif action == 'tvLanguages':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().languages()


elif action == 'tvCertificates':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().certifications()


elif action == 'tvPersons':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().persons(url)


elif action == 'tvUserlists':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().userlists()



####################################################
# SEASON
####################################################

elif action == 'seasons':
    from resources.lib.indexers import seasons
    seasons.seasons().get(tvshowtitle, year, imdb, tvdb)



####################################################
# EPISODES
####################################################

elif action == 'episodes':
    from resources.lib.indexers import episodes
    episodes.episodes().get(tvshowtitle, year, imdb, tvdb, season, episode)


elif action == 'tvWidget':
    from resources.lib.indexers import episodes
    episodes.episodes().widget()


elif action == 'calendar':
    from resources.lib.indexers import episodes
    episodes.episodes().calendar(url)


elif action == 'calendars':
    from resources.lib.indexers import episodes
    episodes.episodes().calendars()


elif action == 'episodesUnfinished':
    from resources.lib.indexers import episodes
    episodes.episodes().unfinished()


elif action == 'episodesUserlists':
    from resources.lib.indexers import episodes
    episodes.episodes().userlists()



####################################################
#---Tools
####################################################

elif action == 'download':
    import json
    from resources.lib.modules import sources
    from resources.lib.modules import downloader
    try: downloader.download(name, image, sources.sources().sourcesResolve(json.loads(source)[0], True))
    except: pass


elif action == 'downloadNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().downloads()


elif action == 'libraryNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().library()


elif action == 'toolNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().tools()


elif action == 'searchNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().search()


elif action == 'viewsNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().views()


elif action == 'refresh':
    from resources.lib.modules import control
    control.refresh()


elif action == 'queueItem':
    from resources.lib.modules import control
    control.queueItem()


elif action == 'openSettings':
    from resources.lib.modules import control
    control.openSettings(query)


elif action == 'open.Settings.CacheProviders':
    from resources.lib.modules import control
    control.openSettings(query)


elif action == 'artwork':
    from resources.lib.modules import control
    control.artwork()


elif action == 'addView':
    from resources.lib.modules import views
    views.addView(content)



####################################################
#---Playcount
####################################################

elif action == 'moviePlaycount':
    from resources.lib.modules import playcount
    playcount.movies(imdb, query)


elif action == 'episodePlaycount':
    from resources.lib.modules import playcount
    playcount.episodes(imdb, tvdb, season, episode, query)


elif action == 'tvPlaycount':
    from resources.lib.modules import playcount
    playcount.tvshows(name, imdb, tvdb, season, query)



####################################################
#---Trakt
####################################################

elif action == 'traktManager':
    from resources.lib.modules import trakt
    trakt.manager(name, imdb, tvdb, season, episode)
    # trakt.manager2(name, imdb, tvdb, season, episode)

elif action == 'authTrakt':
    from resources.lib.modules import trakt
    trakt.authTrakt()
    if params['opensettings'] == 'true':
        control.openSettings(query, "plugin.video.venom")



####################################################
#---Player
####################################################

elif action == 'play':
    from resources.lib.modules import sources
    sources.sources().play(title, year, imdb, tvdb, season, episode, tvshowtitle, premiered, meta, select)


elif action == 'playItem':
    from resources.lib.modules import sources
    sources.sources().playItem(title, source)


elif action == 'trailer':
    from resources.lib.modules import trailer
    trailer.trailer().play(name, url, windowedtrailer)

elif action == 'addItem':
    from resources.lib.modules import sources
    sources.sources().addItem(title)


elif action == 'alterSources':
    from resources.lib.modules import sources
    sources.sources().alterSources(url, meta)


elif action == 'random':
    rtype = params.get('rtype')
    if rtype == 'movie':
        from resources.lib.indexers import movies
        rlist = movies.movies().get(url, create_directory=False)
        r = sys.argv[0]+"?action=play"
    elif rtype == 'episode':
        from resources.lib.indexers import episodes
        rlist = episodes.episodes().get(tvshowtitle, year, imdb, tvdb, season, create_directory=False)
        r = sys.argv[0]+"?action=play"
    elif rtype == 'season':
        from resources.lib.indexers import episodes
        rlist = episodes.seasons().get(tvshowtitle, year, imdb, tvdb, create_directory=False)
        r = sys.argv[0]+"?action=random&rtype=episode"
    elif rtype == 'show':
        from resources.lib.indexers import tvshows
        rlist = tvshows.tvshows().get(url, create_directory=False)
        r = sys.argv[0]+"?action=random&rtype=season"
    from resources.lib.modules import control
    from random import randint
    import json
    try:
        rand = randint(1,len(rlist))-1
        for p in ['title','year','imdb','tvdb','season','episode','tvshowtitle','premiered','select']:
            if rtype == "show" and p == "tvshowtitle":
                try: r += '&'+p+'='+urllib.quote_plus(rlist[rand]['title'])
                except: pass
            else:
                try: r += '&'+p+'='+urllib.quote_plus(rlist[rand][p])
                except: pass
        try: r += '&meta='+urllib.quote_plus(json.dumps(rlist[rand]))
        except: r += '&meta='+urllib.quote_plus("{}")
        if rtype == "movie":
            try: control.infoDialog(rlist[rand]['title'], control.lang(32536).encode('utf-8'), time=30000)
            except: pass
        elif rtype == "episode":
            try: control.infoDialog(rlist[rand]['tvshowtitle']+" - Season "+rlist[rand]['season']+" - "+rlist[rand]['title'], control.lang(32536).encode('utf-8'), time=30000)
            except: pass
        control.execute('RunPlugin(%s)' % r)
    except:
        control.infoDialog(control.lang(32537).encode('utf-8'), time=8000)



####################################################
#----Library Actions
####################################################

elif action == 'movieToLibrary':
    from resources.lib.modules import libtools
    libtools.libmovies().add(name, title, year, imdb, tmdb)


elif action == 'moviesToLibrary':
    from resources.lib.modules import libtools
    libtools.libmovies().range(url)


elif action == 'moviesToLibrarySilent':
    from resources.lib.modules import libtools
    libtools.libmovies().silent(url)


elif action == 'tvshowToLibrary':
    from resources.lib.modules import libtools
    libtools.libtvshows().add(tvshowtitle, year, imdb, tvdb)


elif action == 'tvshowsToLibrary':
    from resources.lib.modules import libtools
    libtools.libtvshows().range(url)


elif action == 'tvshowsToLibrarySilent':
    from resources.lib.modules import libtools
    libtools.libtvshows().silent(url)


elif action == 'updateLibrary':
    from resources.lib.modules import libtools
    libtools.libepisodes().update(query)


elif action == 'service':
    from resources.lib.modules import libtools
    libtools.libepisodes().service()





####################################################
#---Clear Cache actions
####################################################

elif action == 'cfNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().cf()


elif action == 'clearCache':
    from resources.lib.indexers import navigator
    navigator.navigator().clearCache()


elif action == 'clearCacheSearch':
    from resources.lib.indexers import navigator
    navigator.navigator().clearCacheSearch()


elif action == 'clearAllCache':
    from resources.lib.indexers import navigator
    navigator.navigator().clearCacheAll()


elif action == 'clearMetaCache':
    from resources.lib.indexers import navigator
    navigator.navigator().clearCacheMeta()


elif action == 'clearSources':
    from resources.lib.modules import sources
    sources.sources().clearSources()
    if params['opensettings'] == 'true':
        control.openSettings(query, "plugin.video.venom")



####################################################
#---Provider Source actions
####################################################

elif action == 'openscrapersSettings':
    from resources.lib.modules import control
    control.openSettings('0.0', 'script.module.openscrapers')
    # if params['opensettings'] == 'true':
        # control.openSettings(query, "plugin.video.venom")


elif action == 'urlResolver':
    try: import resolveurl
    except: pass
    resolveurl.display_settings()


elif action == 'urlResolverRDTorrent':
    from resources.lib.modules import control
    control.openSettings(query, "script.module.resolveurl")


elif action == "toggleAll":
    sourcelist = []
    from resources.lib import sources
    sourceList = sources.all_providers
    for i in sourceList:
        source_setting = 'provider.' + i
        control.setSetting(source_setting, params['setting'])
#    xbmc.log('All providers = %s' % sourceList,2)
    control.openSettings(query, "plugin.video.venom")


elif action == "toggleAllHosters":
    sourcelist = []
    from resources.lib import sources
    sourceList = sources.hoster_providers
    for i in sourceList:
        source_setting = 'provider.' + i
        control.setSetting(source_setting, params['setting'])
#    xbmc.log('All Hoster providers = %s' % sourceList,2)
    control.openSettings(query, "plugin.video.venom")


elif action == "toggleAllForeign":
    sourcelist = []
    from resources.lib import sources
    sourceList = sources.all_foreign_providers
    for i in sourceList:
        source_setting = 'provider.' + i
        control.setSetting(source_setting, params['setting'])
#    xbmc.log('All Foregin providers = %s' % sourceList,2)
    control.openSettings(query, "plugin.video.venom")


elif action == "toggleAllSpanish":
    sourcelist = []
    from resources.lib import sources
    sourceList = sources.spanish_providers
    for i in sourceList:
        source_setting = 'provider.' + i
        control.setSetting(source_setting, params['setting'])
#    xbmc.log('All Spanish providers = %s' % sourceList,2)
    control.openSettings(query, "plugin.video.venom")


elif action == "toggleAllGerman":
    sourcelist = []
    from resources.lib import sources
    sourceList = sources.german_providers
    for i in sourceList:
        source_setting = 'provider.' + i
        control.setSetting(source_setting, params['setting'])
#    xbmc.log('All German providers = %s' % sourceList,2)
    control.openSettings(query, "plugin.video.venom")


elif action == "toggleAllGreek":
    sourcelist = []
    from resources.lib import sources
    sourceList = sources.greek_providers
    for i in sourceList:
        source_setting = 'provider.' + i
        control.setSetting(source_setting, params['setting'])
#    xbmc.log('All Greek providers = %s' % sourceList,2)
    control.openSettings(query, "plugin.video.venom")


elif action == "toggleAllPolish":
    sourcelist = []
    from resources.lib import sources
    sourceList = sources.polish_providers
    for i in sourceList:
        source_setting = 'provider.' + i
        control.setSetting(source_setting, params['setting'])
#    xbmc.log('All Polish providers = %s' % sourceList,2)
    control.openSettings(query, "plugin.video.venom")


elif action == "toggleAllPaid":
    sourcelist = []
    from resources.lib import sources
    sourceList = sources.all_paid_providers
    for i in sourceList:
        source_setting = 'provider.' + i
        control.setSetting(source_setting, params['setting'])
#    xbmc.log('All Paid providers = %s' % sourceList,2)
    control.openSettings(query, "plugin.video.venom")


elif action == "toggleAllDebrid":
    sourcelist = []
    from resources.lib import sources
    sourceList = sources.debrid_providers
    for i in sourceList:
        source_setting = 'provider.' + i
        control.setSetting(source_setting, params['setting'])
#    xbmc.log('All Debrid providers = %s' % sourceList,2)
    control.openSettings(query, "plugin.video.venom")


elif action == "toggleAllTorrent":
    sourceList = []
    from resources.lib import sources
    sourceList = sources.torrent_providers
    for i in sourceList:
        source_setting = 'provider.' + i
        control.setSetting(source_setting, params['setting'])
#    xbmc.log('All Torrent providers = %s' % sourceList,2)
    control.openSettings(query, "plugin.video.venom")


if action == "toggleDefaults":
    sourcelist = []
    from resources.lib import sources
    sourceList = sources.all_providers
    for i in sourceList:
        source_setting = 'provider.' + i
        default = control.getSettingDefault(source_setting)
        control.setSetting(source_setting, default)
#    xbmc.log('All providers = %s' % sourceList,2)
    control.openSettings(query, "plugin.video.venom")

