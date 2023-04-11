from AmazonAdsLocation import AmazonAdsLocation

class AmazonURLGenerator:
    def createURL(self, location : AmazonAdsLocation, clientId: str, scope : str) -> str:
        url: str = ""
        url += location.value[0]
        url += "?client_id="
        url += clientId
        url += "&scope="
        url += scope
        url += "&response_type=code&redirect_uri="
        url += "https://127.0.0.1:9999"

        
        return url