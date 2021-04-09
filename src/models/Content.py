class Content:
    """
    Common base class for all articles/pages
    """

    def __init__(self, topic, url, title, body):
        self.topic = topic
        self.title = title
        self.body = body
        self.url = url

    def print(self):
        """
        Flexible printing function controls output
        """
        print("New article found for topic: {}").format(self.topic))
        print("TITLE: {}").format(self.title))
        print("BODY: {}").format(self.body))
        print("URL: {}").format(self.url))