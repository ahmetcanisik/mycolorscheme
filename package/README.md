# Convert tailwindcolors to css :root selector variables v0.0.9

I would like to explain the reason for creating this repo in the following lines;
I was using Nextjs 14 and I started using tailwind's gorgeous colors by including tailwindcss in my project. However, there was a problem that I could not set the dark theme. I know the dark: selector is one of the great features of tailwind, but it only worked when the prefers-color-scheme: dark was set, and this did not allow you to switch between the dark and light theme with your own hands. During this process, I received a lot of error messages from NextJS, definitely a theme change. The button was not working. So I downloaded next-themes and believe me, it did the job well enough for me, but following these steps in every new project became so important to me that I decided to create my own css:root selector and save the tailwind codes as variables.

Additionally, creating these color codes has become very useful in my normal HTML projects. I started using this in every project.

> [!NOTE]   
> `:root`     
> `@media (prefers-color-scheme: dark)`    
> `[data-theme="light"]` and `[data-them="dark"]` selectors are available in this project.     

## How to use?

To use it, it is enough to have basic CSS knowledge. here is a usage example:

```css

/* You can also include it in your project via cdn. */
@import url("https://cdn.jsdelivr.net/npm/mycolorscheme@0.0.9/mytheme.min.css")

body {
    background-color: var(--slate-50); /* sets the background color of the page to white for light and black for dark */
    color: var(--slate-950); /* sets the text color of the page to black for light and white for dark */
}
```