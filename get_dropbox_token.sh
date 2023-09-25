curl https://api.dropbox.com/oauth2/token \
    -d code=eLzI5_OmEwAAAAAAAAAAaiPaaW3sxosMw8FeowblnF0 \
    -d grant_type=authorization_code \
    -u 4yl9t4prpzubk4b:mt89pnneqe9nfnv > response.env

refresh_token=$(cat response.env | jq -r '.refresh_token')

echo "DROPBOX_REFRESH_TOKEN=$refresh_token" >> $GITHUB_ENV