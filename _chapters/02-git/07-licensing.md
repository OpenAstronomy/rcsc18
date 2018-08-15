---
interact_link: notebooks/02-git/07-licensing.ipynb
title: 'Licensing'
permalink: 'chapters/02-git/07-licensing'
previouschapter:
  url: chapters/02-git/06-remotes
  title: 'Remotes'
nextchapter:
  url: chapters/02-git/08-citation
  title: 'Citation'
redirect_from:
  - 'chapters/02-git/07-licensing'
---

## Licensing

When a repository with source code, a manuscript or other creative works becomes public, it should include a file LICENSE or LICENSE.txt in the base directory of the repository that clearly states under which license the content is being made available. This is because creative works are automatically eligible for intellectual property (and thus copyright) protection. Reusing creative works without a license is dangerous, because the copyright holders could sue you for copyright infringement.

A license solves this problem by granting rights to others (the licensees) that they would otherwise not have. What rights are being granted under which conditions differs, often only slightly, from one license to another. In practice, a few licenses are by far the most popular, and choosealicense.com will help you find a common license that suits your needs. Important considerations include:

- Whether you want to address patent rights.
- Whether you require people distributing derivative works to also distribute their source code.
- Whether the content you are licensing is source code.
- Whether you want to license the code at all.

Choosing a license that is in common use makes life easier for contributors and users, because they are more likely to already be familiar with the license and don’t have to wade through a bunch of jargon to decide if they’re ok with it. The Open Source Initiative and Free Software Foundation both maintain lists of licenses which are good choices.

This article provides an excellent overview of licensing and licensing options from the perspective of scientists who also write code.

At the end of the day what matters is that there is a clear statement as to what the license is. Also, the license is best chosen from the get-go, even if for a repository that is not public. Pushing off the decision only makes it more complicated later, because each time a new collaborator starts contributing, they, too, hold copyright and will thus need to be asked for approval once a license is chosen.

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #eec275; padding-bottom: 5px;'><h3>Can I Use Open License?</h3>
<p>Find out whether you are allowed to apply an open license to your software. Can you do this unilaterally, or do you need permission from someone in your institution? If so, who?</p></div>

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #eec275; padding-bottom: 5px;'><h3>What licenses have I already accepted?</h3>
<p>Many of the software tools we use on a daily basis (including in this workshop) are released as open-source software. Pick a project on GitHub from the list below, or one of your own choosing. Find its license (usually in a file called LICENSE or COPYING) and talk about how it restricts your use of the software. Is it one of the licenses discussed in this session? How is it different?</p>
<ul>
<li>Git, the source-code management tool</li>
<li>CPython, the standard implementation of the Python language</li>
<li>Jupyter, the project behind the web-based Python notebooks we’ll be using</li>
<li>EtherPad, a real-time collaborative editor</li>
</ul></div>

<div style='padding-left: 5px; padding-top: 0; padding-bottom: 0; padding-right: 0; border: 1px solid; border-color: #7ae78e; padding-bottom: 5px;'><h3>Key Points</h3>
<ul>
<li>People who incorporate General Public License (GPL’d) software into their own software must make their software also open under the GPL license; most other open licenses do not require this.</li>
<li>The Creative Commons family of licenses allow people to mix and match requirements and restrictions on attribution, creation of derivative works, further sharing, and commercialization.</li>
<li>People who are not lawyers should not try to write licenses from scratch.</li>
</ul></div>
