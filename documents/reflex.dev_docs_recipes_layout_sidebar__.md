# Sidebar

Similar to a navigation bar, a sidebar is a common UI element found on the side of a webpage or application. It typically contains links to different sections of the site or app.

[View Example](https://reflex.dev/docs/recipes/layout/sidebar/#basic)

# Basic

UI

## Code

```python
import some_module

def some_function():
    print("Hello, World!")
```

UI

# Reflex

<a href="/">
    <div>
        <svg class="lucide lucide-layout-dashboard">
            <rect height="9" rx="1" width="7" x="3" y="3"/>
            <rect height="5" rx="1" width="7" x="14" y="3"/>
            <rect height="9" rx="1" width="7" x="14" y="12"/>
            <rect height="5" rx="1" width="7" x="3" y="16"/>
        </svg>
        Dashboard
    </div>
</a>

<a href="/">
    <div>
        <svg class="lucide lucide-square-library">
            <rect height="18" rx="2" width="18" x="3" y="3"/>
            <path d="M7 7v10"/>
            <path d="M11 7v10"/>
            <path d="m15 7 2 10"/>
        </svg>
        Projects
    </div>
</a>

<a href="/">
    <div>
        <svg class="lucide lucide-chart-column-increasing">
            <path d="M13 17V9"/>
            <path d="M18 17V5"/>
            <path d="M3 3v16a2 2 0 0 0 2 2h16"/>
            <path d="M8 17v-3"/>
        </svg>
        Analytics
    </div>
</a>

<a href="/">
    <div>
        <svg class="lucide lucide-mail">
            <rect height="16" rx="2" width="20" x="2" y="4"/>
            <path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>
        </svg>
        Messages
    </div>
</a>

<a href="/">
    <div>
        <svg class="lucide lucide-settings">
            <path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0 .73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z"/>
            <circle cx="12" cy="12" r="3"/>
        </svg>
        Settings
    </div>
</a>

<a href="/">
    <div>
        <svg class="lucide lucide-log-out">
            <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/>
            <polyline points="16 17 21 12 16 7"/>
            <line x1="21" x2="9" y1="12" y2="12"/>
        </svg>
        Log out
    </div>
</a>

<span class="rt-Separator rt-r-orientation-horizontal"></span>

<div>
    <button>
        <svg class="lucide lucide-user">
            <path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/>
            <circle cx="12" cy="7" r="4"/>
        </svg>
    </button>

    <div>
        My account
        user@reflex.dev
    </div>
</div>

<div>
    <svg class="lucide lucide-align-justify">
        <path d="M3 12h18"/>
        <path d="M3 18h18"/>
        <path d="M3 6h18"/>
    </svg>
</div>

<a href="https://reflex.dev/docs/recipes/layout/sidebar/#top-user-profile">
    <h2 id="top-user-profile">Top user profile</h2>
    <svg class="lucide lucide-link">
        <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/>
        <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/>
    </svg>
</a>

<div class="rt-TabsRoot">
    <div role="tablist" tabindex="0">
        <button id="radix-:Rkmkml6:-trigger-tab1" aria-selected="true" type="button">
            UI
        </button>
        <button id="radix-:Rkmkml6:-trigger-tab2" aria-selected="false" type="button">
            Code
        </button>
    </div>

    <div role="tabpanel" tabindex="0" id="radix-:Rkmkml6:-content-tab1" data-state="active">
        <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
            <button>
                <svg class="lucide lucide-user">
                    <path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/>
                    <circle cx="12" cy="7" r="4"/>
                </svg>
            </button>

            <div>My account</div>
            user@reflex.dev

            <button>
                <svg class="lucide lucide-settings">
                    <path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0 .73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z"/>
                    <circle cx="12" cy="12" r="3"/>
                </svg>
            </button>

            <div class="rt-Flex">
                <a href="/">
                    <div>Dashboard</div>
                </a>
                <a href="/">
                    <div>Projects</div>
                </a>
                <a href="/">
                    <div>Analytics</div>
                </a>
                <a href="/">
                    <div>Messages</div>
                </a>
                <a href="/">
                    <div>Help &amp; Support</div>
                </a>
            </div>

            <svg class="lucide lucide-align-justify">
                <path d="M3 12h18"/>
                <path d="M3 18h18"/>
                <path d="M3 6h18"/>
            </svg>
        </div>
    </div>

    <div role="tabpanel" tabindex="0" id="radix-:Rkmkml6:-content-tab2" hidden data-state="inactive">
        Content for tab 2
    </div>
</div>

# Bottom user profile

## UI
<div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
<div class="rt-Box css-1v8fzbk">
<div class="rt-Flex rt-r-fd-column rt-r-ai-start rt-r-gap-5 rx-Stack css-f6xktk">
<div class="rt-Flex rt-r-fd-row rt-r-ai-center rt-r-jc-start rt-r-gap-3 rx-Stack css-4bgxf5">
<img class="css-1jjl46k" src="/logo.jpg"/>
</div>
</div>
</div>
</div>

# Reflex

[Dashboard](/#)
[Projects](/#)
[Analytics](/#)
[Messages](/#/)

---

[Settings](/#)
[Log out](/#/)

**My account**
- user@reflex.dev

---

# Top user profile

UI

- **My account**: user@reflex.dev
  - Profile Picture
  - Settings

## Dashboard
- ![Dashboard](/#)

## Projects
- ![Projects](/#)

## Analytics
- ![Analytics](/#)

## Messages
- ![Messages](/#)

## Help & Support
- ![Help & Support](/#)