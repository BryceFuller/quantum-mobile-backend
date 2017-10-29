# Before you can use the jobs API, you need to set up an access token.
# Log in to the Quantum Experience. Under "Account", generate a personal 
# access token. Replace "None" below with the quoted token string.
# Uncomment the APItoken variable, and you will be ready to go.

APItoken = "146c496f3eba88c39995b0e32445c9dea4a0955512b9b005c1bdef2c6e8df2ff42d3e28e25e064db80d6ce0a7d5b996b8d3f95cde94848df1c850b0a80fdc822"

config = {
  "url": 'https://quantumexperience.ng.bluemix.net/api'
}

if 'APItoken' not in locals():
  raise Exception("Please set up your access token. See Qconfig.py.")
