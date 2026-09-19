from pathlib import Path
import json, shutil, re
root=Path(__file__).parent
d=root/'dist'
backup=root/'archive-before-slate'
backup.mkdir(exist_ok=True)
for f in ['index.html','style.css','app.js','media.js']:
 if not (backup/f).exists(): shutil.copy2(d/f,backup/f)
rows=json.loads((root/'content.json').read_text())
heads=['Make your next<br>move matter.','Your story.<br>Made social.','A stay worth<br>discovering.','Give them a<br>reason to visit.','Small shop.<br>New possibilities.','Made by hand.<br>Remembered by heart.','Build a brand<br>they remember.','Go live.<br>Get closer.','Your ambition.<br>Our everyday work.','Let’s grow,<br>together.']
eyes=['REAL STORIES · BIGGER TOMORROWS','IDEAS INTO EVERYDAY IMPACT','HOTELS & HOSPITALITY','RESTAURANTS & CAFÉS','LOCAL SHOPS & ONLINE SELLERS','HANDMADE & HERITAGE','LOCAL BRANDS','LIVE COMMERCE','YOUR GROWTH TEAM','YOUR NEXT CHAPTER']
desc=['Content that tells your story.<br>Social media that keeps it moving.','Planning, photography, short videos and everyday publishing.','From a first impression to the feeling of being there. Bring your rooms, service and experience into focus.','From the kitchen to the feed. Make your food, people and atmosphere part of the story.','Show what makes your products special, with clear visuals and social support that fits your day.','Bring the process, the people and the care behind every piece into the spotlight.','A recognisable look, a consistent voice and content that carries your story across every channel.','Product demonstrations, live session planning and real-time audience support.','From a single shoot to ongoing page management. Choose the support your business needs.','Tell us about your business, your audience and what you want to do next. We’ll shape the next step together.']
labels=['Explore services','See what we do','Plan a hotel shoot','Create a food story','Support my shop','Tell my craft story','Build my brand','Explore live support','Compare plans','Copy Facebook Page name']
tags=[['Content','Social','Live'],['Photography','Short video','Publishing'],['Room stories','Guest experience','Campaigns'],['Menu content','Reels','Local discovery'],['Product shoots','Shop stories','Social support'],['Maker stories','Process films','Product details'],['Visual direction','Brand voice','Launch content'],['Live planning','Product demos','Audience replies'],['Plan','Create','Publish'],['Yangon, Myanmar','Burmese & English']]
head='''<!doctype html><html lang="my"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="#14263d"><title>Business Growth Myanmar — Content, Social & Live</title><meta name="description" content="Content creation, social media management and live commerce for Myanmar businesses."><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Noto+Sans+Myanmar:wght@400;500;600&display=swap" rel="stylesheet"><link rel="stylesheet" href="style.css?v=slate1"></head><body><a class="skip" href="#city">Skip to content</a><header class="glass"><a class="brand" href="#city" aria-label="Business Growth Myanmar home"><span class="monogram">bgm</span><span>BUSINESS GROWTH<br>MYANMAR</span></a><nav aria-label="Main navigation"><a href="#content">Services</a><a href="#hotel">Industries</a><a href="#plans">Plans</a></nav><a class="button primary nav-contact" href="#contact">Let's talk</a></header><aside class="rail" aria-label="Scene navigation">'''
head+=''.join(f'<a href="#{r[0]}" aria-label="{i+1:02d} {eyes[i]}" title="{eyes[i]}">{i+1:02d}</a>' for i,r in enumerate(rows))
head+='</aside><button class="motion glass" aria-pressed="false">Pause motion</button><main>'
plans='''<section class="plans" id="plans" aria-labelledby="plans-title"><div class="plans-intro"><p class="eyebrow">A LITTLE SUPPORT. OR THE WHOLE PICTURE.</p><h2 id="plans-title">The right team.<br>The right plan.</h2><p class="my">သင့်အတွက် ဘယ် Plan လဲ။</p><p>လုပ်ငန်းလိုအပ်ချက်အလိုက် ဝန်ဆောင်မှုများကို ညှိနှိုင်းနိုင်ပါတယ်။</p></div><div class="plan-grid">'''
packages=[('CREATE','Content Studio','အမှတ်တံဆိပ်ကို ထင်ရှားစေဖို့။','For businesses that need a fresh library of content.',['Content planning','Product & business photography','Short-form video editing','Myanmar & English captions']),('MANAGE','Social Management','နေ့စဉ် Social Media အတွက်။','For businesses that want a consistent social presence.',['Content Studio support','Monthly content calendar','Publishing & community replies','Monthly performance review']),('CONNECT','Live Commerce','Live အစမှ အဆုံးအထိ အတူရှိမယ်။','For businesses ready to connect with customers live.',['Live session planning','Product demo preparation','Livestream production support','Audience & enquiry coordination'])]
for i,(tag,title,my,description,features) in enumerate(packages):
 plans+=f'<article class="glass"><p class="eyebrow">0{i+1} / {tag}</p><h3>{title}</h3><p lang="my">{my}</p><p class="plan-desc">{description}</p><ul>'+''.join(f'<li>{f}</li>' for f in features)+f'</ul><a class="button {"primary" if i==1 else "secondary"} plan-select" href="#contact" data-plan="{title}">Discuss this plan</a></article>'
plans+='</div><p class="plan-note">Scope & pricing tailored to your business. Advertising spend quoted separately.</p></section>'
body=''
for i,r in enumerate(rows):
 ident,asset,_,my,*_=r
 tag='h1' if i==0 else 'h2'
 body+=f'<section id="{ident}" class="hero {"right" if i%2 else "left"}" data-index="{i}" aria-labelledby="title-{ident}"><div class="visual"><img src="assets/{asset}.webp" alt="{eyes[i].title()} — Business Growth Myanmar" loading="{"eager" if i==0 else "lazy"}" {"fetchpriority=high" if i==0 else ""} width="1672" height="941"><video muted playsinline loop preload="none" poster="assets/{asset}.webp" aria-hidden="true"></video></div><div class="shade"></div><div class="hero-copy"><p class="eyebrow">{eyes[i]}</p><{tag} id="title-{ident}" lang="en">{heads[i]}</{tag}><p class="my">{my}</p><p class="desc" lang="en">{desc[i]}</p>'
 if i==0:
  body+='<div class="platforms" aria-label="Social platforms"><span class="glass">Facebook</span><span class="glass">Instagram</span><span class="glass">TikTok</span></div>'
 elif i==9:
  body+='<p id="selected-plan" hidden></p><p class="page-name">Facebook · Business Growth Myanmar</p><button class="button primary copy-page">Copy Facebook Page name</button><p class="contact-note">ဒီနာမည်ကို Facebook မှာ ရှာနိုင်ပါတယ်။</p>'
 else:
  body+=f'<a class="button primary" href="#{"services" if i==1 else "plans"}">{labels[i]}</a>'
 body+='</div>'
 if i==0:
  body+='<div class="hero-dock glass"><div class="dock-actions"><a class="button primary" href="#content">Explore services</a><a class="button secondary" href="#plans">Choose a plan</a></div><div class="dock-services"><a href="#content">Content</a><a href="#services">Social</a><a href="#live">Live</a></div></div>'
 else:
  body+='<div class="section-bottom">'+''.join(f'<span>{t}</span>' for t in tags[i])+f'<small>{i+1:02d} / 10</small></div>'
 body+='</section>'
 if i==8: body+=plans
foot='''</main><footer><strong>Business Growth Myanmar</strong><span>Content. Community. Commerce.</span><a href="#city">Back to top</a></footer><div id="toast" role="status" aria-live="polite"></div><dialog id="copy-dialog"><h2>Find our Facebook Page</h2><p>Business Growth Myanmar</p><p>ဒီနာမည်ကို Facebook မှာ ရှာနိုင်ပါတယ်။</p><button class="button primary" id="close-dialog">Close</button></dialog><script src="media.js"></script><script src="app.js?v=slate1"></script></body></html>'''
(d/'index.html').write_text(head+body+foot)
