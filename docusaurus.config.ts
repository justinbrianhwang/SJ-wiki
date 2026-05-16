import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

const config: Config = {
  title: 'Sunjun Hwang | Wiki',
  titleDelimiter: '·',
  tagline: 'Notes on Mathematics, Computer Science, Physics & Chemistry',
  favicon: 'img/logo.png',

  future: {
    v4: true,
  },

  url: 'https://sjhwangwiki.com',
  baseUrl: '/',

  organizationName: 'justinbrianhwang',
  projectName: 'SJ-wiki',
  deploymentBranch: 'gh-pages',
  trailingSlash: false,

  onBrokenLinks: 'warn',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  markdown: {
    mermaid: true,
    hooks: {
      onBrokenMarkdownLinks: 'warn',
    },
  },
  themes: ['@docusaurus/theme-mermaid'],

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          routeBasePath: '/',
          editUrl:
            'https://github.com/justinbrianhwang/SJ-wiki/tree/main/',
          remarkPlugins: [remarkMath],
          rehypePlugins: [rehypeKatex],
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  stylesheets: [
    {
      href: 'https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css',
      type: 'text/css',
      integrity:
        'sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV',
      crossorigin: 'anonymous',
    },
  ],

  themeConfig: {
    image: 'img/social-card.png',
    colorMode: {
      defaultMode: 'light',
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'SJ Wiki',
      logo: {
        alt: 'SJ Wiki Logo',
        src: 'img/logo.png',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'mathSidebar',
          position: 'left',
          label: 'Math',
        },
        {
          type: 'docSidebar',
          sidebarId: 'csSidebar',
          position: 'left',
          label: 'CS',
        },
        {
          type: 'docSidebar',
          sidebarId: 'physicsSidebar',
          position: 'left',
          label: 'Physics',
        },
        {
          type: 'docSidebar',
          sidebarId: 'chemSidebar',
          position: 'left',
          label: 'Chemistry',
        },
        {
          type: 'docSidebar',
          sidebarId: 'qisSidebar',
          position: 'left',
          label: 'Quantum Info',
        },
        {
          href: 'https://www.sjhwang.com',
          label: 'sjhwang.com',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Subjects',
          items: [
            {label: 'Mathematics', to: '/math'},
            {label: 'Computer Science', to: '/cs'},
            {label: 'Physics', to: '/physics'},
            {label: 'Chemistry', to: '/chemistry'},
            {label: 'Quantum Information Science', to: '/quantum-information-science'},
          ],
        },
        {
          title: 'More',
          items: [
            {
              label: 'Personal site',
              href: 'https://www.sjhwang.com',
            },
            {
              label: 'GitHub',
              href: 'https://github.com/justinbrianhwang/SJ-wiki',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} SJ Wiki. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: ['python', 'c', 'cpp', 'java', 'bash', 'matlab'],
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
