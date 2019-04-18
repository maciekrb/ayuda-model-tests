from datetime import datetime, timedelta
from pydantic import BaseModel


class AyudaPlay(BaseModel):
    """ Ayuda Playlog Model.  """

    SiteCode: str
    AdvertiserName: str
    DigitalFaceCode: str
    MediaFileName: str
    PlayToEnd: bool
    DesignDuration: int
    SpotLength: int
    EndTime: datetime

    def _duration(self):
        """ Ayuda duration computation according to insight provided by
            Jarnail Singh 2019-04-16 """
        if self.PlayToEnd is True and self.DesignDuration > 0:
            return self.DesignDuration

        elif self.PlayToEnd is True and self.DesignDuration == 0:
            return self.SpotLength

        elif self.PlayToEnd is False and self.DesignDuration == 0:
            return self.SpotLength

        elif self.PlayToEnd is False and self.DesignDuration < self.SpotLength:
            return self.DesignDuration

        else:
            # Two conditions might end up here:
            #   * PlayToEnd is False and DesignDuration >= spotLength
            #   * PlayToEnd is True and DesignDuration < 0
            return self.SpotLength

    def _start_time(self):
        return self.EndTime - timedelta(seconds=self._duration())

    def _end_time(self):
        return self.EndTime
