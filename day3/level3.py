#playlist matching using Linked Lists 

#KEY TAKEAWAYS: LINKED LIST 

class node:
    def __init__(self, label):
        self.label = label
        self.next = None

class myPlaylist:
    def __init__(self):
        self.head = node("PLAYLIST1")
        pass

    def addSong(self, label):
        head = self.head

        while head.next is not None:
            head = head.next
        newSong = node(label)
        head.next = newSong
        return "Song Added"

    def viewPlaylist(self, head=None):
        head = head or self.head

        while head.next is not None:
            print(head.label, end=" -> ")
            head = head.next
        print(head.label)

    def reversePlaylist(self):
        prev = None
        current = self.head
        
        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode

        self.viewPlaylist(prev)

playlist = myPlaylist()
playlist.addSong("1")
playlist.addSong("2")
playlist.addSong("3")
playlist.addSong("4")
playlist.addSong("5")
playlist.viewPlaylist()
playlist.reversePlaylist()