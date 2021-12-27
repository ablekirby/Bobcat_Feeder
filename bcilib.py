# Bobcat Feeder library, XML generation, data management and file io
# Bobcat Index
# Able Kirby

from xml.dom import minidom
from datetime import datetime
import urllib
import eyed3
import os

verstr = "v1.00"

# Top Level classes
#   Application State   bfAPP
#   Song object         bfSONG

# Channel level Tags
#   title
#   description
#   link
#   language
#   generator
#   pubDate
#   webMaster
#   image
#   podcast:medium
#   podcast:locked
#   podcast:category
#   podcast:location
#   podcast:value
#   item

# Item level Tags
#   title
#   description
#   guid
#   pubdate
#   enclosure
#   podcast:season
#   podcast:episode
#   podcast:soundbite

def makeTag(name,text):
    tag = minidom.Document().createElement(name)
    txt = minidom.Document().createTextNode(text)
    tag.appendChild(txt)
    return tag

class bfAPP:
    def __init__(self):
        self.email = "contact@bobcatindex.com"
        self.title = "Example Album Title"
        self.artist = "Example Artist Title"
        self.desc = "Example Description"
        self.link = "Link to album page"
        self.language = "en"
        self.generator = "Bobcat Feeder " + verstr
        self.category = "Fantasy Music Technology"
        self.location = "Ellicott City, MD"
        self.image = "bobcatindex.jpg"
        self.url = "http://www.ablekirby.com/music/"

        self.songs = []
        self.values = []

   
    def clearsongs(self):
        self.songs = []

    def getProjectName(self):
        return self.title + " by " + self.artist
   
    def getfn(self):
        fn = (self.artist + "_" + self.title).replace(' ','')
        return urllib.parse.quote(fn) + ".xml"


    def appendValue(self,name,pubkey,split):
        self.values.append((name,pubkey,split))

    def getLockedTag(self):
        locktag = makeTag("podcast:locked","no")
        locktag.setAttribute("owner",self.email)
        return locktag


    def getValueTag(self):
        valtag = minidom.Document().createElement("podcast:value")
        valtag.setAttribute("type","lightning")
        valtag.setAttribute("method","keysend")
        valtag.setAttribute("suggested","0.00000015000")

        for i in self.values:
            valrec = minidom.Document().createElement("podcast:valueRecipient")
            valrec.setAttribute("name",i[0])
            valrec.setAttribute("address",i[1])
            valrec.setAttribute("split",str(i[2]))
            valtag.appendChild(valrec)

        return valtag

    def getImageTag(self):
        imgtag = minidom.Document().createElement("image")
        imgtag.appendChild(makeTag("url",self.url + urllib.parse.quote(self.image)))
        imgtag.appendChild(makeTag("title",self.title + " Album Cover"))
        imgtag.appendChild(makeTag("link",self.url))
        imgtag.appendChild(makeTag("description",self.title + " Album Cover"))
        return imgtag

    def importMP3(self,fn):
        song = bfSONG.fromMP3(fn)
        self.title = song.album
        self.artist = song.artist
        self.songs.append(song)
    
    def importJPG(self,fn):
        self.image = os.path.basename(fn)

    def getpubdate(self):
        now = datetime.now()
        strtime = now.strftime("%a, %d %b %Y %H:%M:%S")+ " +0000"
        return strtime

    def writeXML(self):

        # RSS level
        root = minidom.Document()
        xml = root.createElement("rss")
        xml.setAttribute("xmlns:podcast","https://github.com/Podcastindex-org/podcast-namespace/blob/main/docs/1.0.md")
        xml.setAttribute("xmlns:itunes","http://www.itunes.com/dtds/podcast-1.0.dtd")
        xml.setAttribute("version","2.0")
        root.appendChild(xml)

        # Channel level
        channel = root.createElement("channel")
        channel.appendChild(makeTag("title",self.title))
        channel.appendChild(makeTag("itunes:author",self.artist))
        channel.appendChild(makeTag("description",self.desc))
        channel.appendChild(makeTag("link",self.link))
        channel.appendChild(makeTag("language",self.language))
        channel.appendChild(makeTag("generator",self.generator))
        channel.appendChild(makeTag("pubDate",self.getpubdate()))
        channel.appendChild(makeTag("lastBuildDate",self.getpubdate()))
        channel.appendChild(self.getLockedTag())
        channel.appendChild(makeTag("podcast:category",self.category))
        channel.appendChild(makeTag("podcast:location",self.location))
        channel.appendChild(makeTag("managingEditor",self.email))
        channel.appendChild(makeTag("webMaster",self.email))
        channel.appendChild(self.getImageTag())
        channel.appendChild(makeTag("podcast:medium","music"))
        channel.appendChild(self.getValueTag())

        # Item level
        for i in self.songs:
            newitem = root.createElement("item")
            newitem.appendChild(makeTag("title",i.title))
            newitem.appendChild(makeTag("description",i.title + " - " + i.artist))
            newitem.appendChild(makeTag("pubdate",self.getpubdate()))

            # enclosure
            enctag = root.createElement("enclosure")
            enctag.setAttribute("url",self.url + urllib.parse.quote(i.fn))
            enctag.setAttribute("length",str(i.nbytes))
            enctag.setAttribute("type","audio/mpeg")
            newitem.appendChild(enctag)

            newitem.appendChild(makeTag("podcast:episode",i.track_num))
            channel.appendChild(newitem)

        # Write to Disk
        xml.appendChild(channel)
        xmlstr = root.toprettyxml(indent = "\t")
        with open(self.getfn(), "w") as f:
            f.write(xmlstr)

class bfSONG:
    def __init__(self,title):
        self.title = title
        self.fn = title + ".mp3"
        self.desc = "Track x"

    @staticmethod
    def fromMP3(fn):
        song = bfSONG("fromMP3")
        try:
            song.nbytes = os.path.getsize(fn)
            #print(fn + " is " + str(song.nbytes) + " bytes long")

        except OSError:
            #print("File does not exist")
            song.nbytes=0

        # eyed3 operations
        af = eyed3.load(fn)
        song.artist = af.tag.artist
        song.album = af.tag.album
        song.title = af.tag.title
        song.fn = os.path.basename(fn)
        song.track_num = str(af.tag.track_num[0])
        song.desc = song.artist + " - " + song.title

        return song

    def getelement(self):
        pass
        # Generate and return the <item> element for this song

#myapp = bfAPP()

#myapp.appendValue("AbleKirby","02f1962328552371769881a9f49c192c0df261f3e0bdf4cd68a4f6d449cc6fd4ad",50)
#myapp.appendValue("SirSpencer","03ecb3ee55ba6324d40bea174de096dc9134cb35d990235723b37ae9b5c49f4f53",50)
#myapp.importMP3("01 - Living In The Future.mp3")
#myapp.importJPG("albumart.jpg")
#myapp.writeXML()
