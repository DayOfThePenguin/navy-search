from pydantic import BaseModel, HttpUrl, validator


class TestUrl(BaseModel):
    # pylint: disable=no-self-argument,no-self-use,invalid-name
    url: HttpUrl

    @validator("url")
    def check_url_props(cls, v):
        assert v.scheme == "https", "scheme must be https"
        assert v.tld == "mil", "top-level domain must be .mil"
        return v


test_object = TestUrl(url="https://www.secnav.navy.mil/doni/notices.aspx")
