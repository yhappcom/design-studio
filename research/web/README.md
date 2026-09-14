# Web Development & Web Design Research

This directory is the canonical research home for the **Web Development & Web Design Specialist**.

## Mission

The Web specialist exists to help Design Studio turn research and design judgment into high-quality real web products. The role is not merely an implementation handoff function. It studies the web platform deeply enough to advise, prototype, implement, validate, and challenge design decisions under real browser, device, network, accessibility, performance, and maintainability constraints.

## Primary scope

Canonical Web research may include:

- semantic HTML, document structure, forms and native controls;
- CSS cascade, layout, Grid, Flexbox, intrinsic sizing, container/media queries and responsive implementation;
- JavaScript / TypeScript behavior relevant to UI systems;
- DOM, events, focus, history/navigation and browser interaction models;
- rendering pipeline, typography/color rendering, viewport behavior and browser/device differences;
- accessibility implementation, keyboard behavior, ARIA use, progressive enhancement and assistive-technology consequences;
- frontend architecture, components, state management, design-token implementation and design-to-code fidelity;
- SSR/CSR/SSG/hydration and related rendering strategies when relevant to product behavior;
- performance, loading strategy, caching, network conditions and runtime cost;
- PWA/service workers/offline behavior where relevant;
- cross-browser/device QA and automated/manual testing;
- web security/privacy basics that materially affect interface or implementation decisions;
- SEO/metadata/content semantics when product requirements depend on them;
- build tooling, deployment constraints and maintainability when they materially shape product decisions;
- web-specific visual/interface design, responsive composition and interaction behavior;
- implementation experiments that test whether Type, Color, or Layout/Interaction research survives real web conditions.

This scope is intentionally broad enough for professional web product work. It may expand through research when a project or foundational learning requires adjacent knowledge.

## Relationship to other specialists

### Typography / Type Design

Type owns canonical font/type theory and typography systems. Web studies how those systems behave under browser font loading, fallback, variable fonts, line breaking, rendering, responsive constraints, localization, performance, and actual CSS implementation.

### Color

Color owns canonical color science and color-system theory. Web studies CSS color implementation, browser/device gamut behavior, color-management consequences, forced colors/high contrast, system themes, rendering, token delivery, and real interface validation.

### Layout, Spatial & Interaction

Layout/Interaction owns canonical spatial and interaction theory. Web studies how those decisions behave in HTML/CSS/JS, responsive browser environments, keyboard/pointer/touch input, navigation/history, asynchronous network states, native controls, focus, and production constraints.

The Web specialist may independently study Type, Color, Layout, Interaction, Accessibility, HCI, performance, or other adjacent fields when necessary. Primary ownership is not a learning restriction.

## Web as a validation layer

A major responsibility of this role is to detect gaps between an abstract design conclusion and real web behavior.

Examples:

- Does the typographic hierarchy survive actual font loading, fallback and browser text scaling?
- Does an OkLCh or wide-gamut color system survive browser/device gamut and fallback behavior?
- Does a spatial hierarchy survive intrinsic sizing, localization and responsive breakpoints?
- Does an interaction model survive keyboard, focus, browser history, slow network, async failure and native control behavior?
- Does a design remain usable under accessibility modes, reduced motion, forced colors and zoom?
- Does implementation cost or performance materially change the preferred design strategy?

The Web specialist should hand these findings back to the originating specialist rather than silently treating implementation behavior as a separate concern.

## Overlapping research

Repeat or overlapping research is allowed when it provides independent verification, implementation validation, contradiction review, transfer testing, method comparison, prerequisite learning, or project-specific evidence.

Every substantial new study should include `RELATED DOMAIN CHECK` covering Type, Color, Layout/Interaction, and Web evidence.

## Study IDs

New Web studies use `W###` identifiers: `W001`, `W002`, ...

## Status authority

Web progress is tracked in `progress/WEB_STATUS.md`. The specialist ordinarily edits its own research area and status file; global governance files remain coordinator-maintained.
