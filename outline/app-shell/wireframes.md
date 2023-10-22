# App Shell - Wireframes

The App Shell should be able to adapt to a few states, and supply all the relevant navigation links accordingly: unauthenticated and authenticated states, viewing static pages and app content states, and within the app, being outside or inside a garden context.

# Static Pages

The [static pages](../static-pages/README.md) are the entry points to the website, including landing page, project page, and donation page.

## Unauth Static Pages

![Unauth Static Pages](./wireframes/unauth-static-pages.excalidraw.png)

A horizontal, top navbar is used for a familiar website-style introduction to the application. 

## Auth Static Pages

The authenticated view of static pages should be the same at the [Auth App Base](#auth-app-base).

# App Base

The App Base applies to any non-static page that isn't within a garden context.

## Unauth App Base

![Unauth App Base](./wireframes/unauth-app-base.excalidraw.png)

The unauthenticated view of the app should be basically the same as the unauthenticated view of the static pages, but match the sidebar configuration of the other cases.

## Auth App Base

![Auth Static Pages](./wireframes/auth-app-base.excalidraw.png)

The authenticated view of the app should give access to the static pages, the main [Garden](../gardens/README.md) menu, and the [User](../users/README.md) menu.

# App Garden

The App Base applies to any non-static page that is within a garden context.

## Unauth App Garden

![Unauth App Garden](./wireframes/unauth-app-garden.excalidraw.png)

The unauthenticated view of a garden should allow access to all the information in that garden, including the dashboard, planner, config, environment, and devices tab. It should still contain Login and Register buttons, as well as a way of getting back to the static pages. 

## Auth App Garden

![Auth App Garden](./wireframes/auth-app-garden.excalidraw.png)

The authenticated view of a garden should allow access to all the information in that garden, as well as retaining the main [Garden](../gardens/README.md) menu, and the [User](../users/README.md) menu.