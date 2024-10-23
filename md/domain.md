<h2 id="fs6Yu">总结</h2>
<h3 id="YW1Vw">域名购买,域名绑定和解析,项目绑定自定义域名教程</h3>
1.[namesilo](https://www.namesilo.com/account/) 购买一个一级域名

2.namesilo管理界面点击 manage

![](./images/1729588490058-d6d47dc4-41ab-45e6-b8f8-02e7ae14222e.png)



点击域名绑定

![](./images/1729588554566-7b551e90-91a0-477f-baff-8a00ef4e0edf.png)

填写cloudflare给的DNS

![](./images/1729588591513-57897992-c876-49a4-a0bd-3b21e8d53ec2.png)

3.打开 [cloudflare](https://dash.cloudflare.com/) 在概述里面填写买的域名 然后将两个名称服务器填写到你购买的域名管理里面进行替换

![](./images/1729588849541-17b0c0a2-091d-44b9-822e-aff6502520ad.png)

4.在 [vercerl](https://vercel.com/) 部署项目以后 将domain填写成你的域名,你可以填写前缀变成一个二级域名使用,如我的是 weijordan.top,那我将设成blog.weijordan.top,将

![](./images/1729589030315-958bafeb-2873-48a4-aa6a-7bc634258b23.png)

![](./images/1729589041236-ceebc322-072c-419b-9a45-ef3b8682255a.png)

![](./images/1729589058866-6d485674-0500-4653-9902-7fe378a3c421.png)

三个填入 [cloudflare](https://dash.cloudflare.com/) 的DNS 管理里面 

![](./images/1729589125119-25183eca-8fb3-42a3-a6fc-99eaa93f9e7d.png)

然后刷新vercel,等待DNS解析,如果暂时没反应,等待24小时左右



---

<h2 id="OayU7">视频教程</h2>
[https://www.bilibili.com/video/BV1mu4y1t7Vm/?spm_id_from=333.337.search-card.all.click&vd_source=ac6ab4c3cdc5d0193edf55fd77ba0b4f](https://www.bilibili.com/video/BV1mu4y1t7Vm/?spm_id_from=333.337.search-card.all.click&vd_source=ac6ab4c3cdc5d0193edf55fd77ba0b4f)



[https://www.bilibili.com/video/BV1NeeVeoEid?spm_id_from=333.788.player.switch&vd_source=ac6ab4c3cdc5d0193edf55fd77ba0b4f](https://www.bilibili.com/video/BV1NeeVeoEid?spm_id_from=333.788.player.switch&vd_source=ac6ab4c3cdc5d0193edf55fd77ba0b4f)



[https://www.wenrui0326.top/article/loudflare-domain-dns-setup-guide](https://www.wenrui0326.top/article/loudflare-domain-dns-setup-guide)

<h2 id="yPCb5">域名管理</h2>
namesilo  
[https://www.namesilo.com/account_domains.php](https://www.namesilo.com/account_domains.php)



<h2 id="VApYu">域名解析 cloudflare</h2>
[https://dash.cloudflare.com/94e4876a7573ff5135ac1c45baa3f712/weijodan.top/dns/records](https://dash.cloudflare.com/94e4876a7573ff5135ac1c45baa3f712/weijodan.top/dns/records)

