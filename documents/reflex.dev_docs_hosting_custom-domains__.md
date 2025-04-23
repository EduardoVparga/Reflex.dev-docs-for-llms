# Custom Domains

With the Pro tier of Reflex Cloud you can use your own custom domain to host your app.

[Learn more](https://reflex.dev/docs/hosting/custom-domains/#prerequisites)

# Prerequisites
You must purchase a domain from a domain registrar such as GoDaddy, Cloudflare, Namecheap, or AWS.

For this tutorial we will use GoDaddy and the example domain `tomgotsman.us`.

[Continue to Steps](https://reflex.dev/docs/hosting/custom-domains/#steps)

# Steps

Once you have purchased your domain, you can add it to your Reflex Cloud app by following these steps:

1. Ensure you have deployed your app to Reflex Cloud.
2. Once your app is deployed click the `Custom Domain` tab and add your custom domain to the input field and press the Add domain button. You should now see a page like below:
![](custom-domains-DNS-inputs.png)

3. On the domain registrar's website, navigate to the DNS settings for your domain. It should look something like the image below:
![](custom-domains-DNS-before.png)

4. Add all four of the DNS records provided by Reflex Cloud to your domain registrar's DNS settings. If there is already an A name record, delete it and replace it with the one provided by Reflex Cloud. Your DNS settings should look like the image below:
![](custom-domains-DNS-after.png)

It may alert you that this record will resolve on ######.tomgotsman.us.tomgotsman.us.

# Your domain provider may not support an Apex CNAME record, in this case just use an A record.

Once you have added the DNS records, refresh the page on the Reflex Cloud page (it may take a few minutes to a few hours to update successfully). If the records are correct, you should see a success message like the one below:
![](custom-domains-success.png)

Now redeploy your app using the `reflex deploy` command and your app should now be live on your custom domain!