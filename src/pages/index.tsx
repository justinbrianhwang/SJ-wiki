import type {ReactNode} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';

import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <img
          src="img/logo.png"
          alt="SJ Wiki Logo"
          className={styles.heroLogo}
        />
        <Heading as="h1" className="hero__title">
          {siteConfig.title}
        </Heading>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
      </div>
    </header>
  );
}

type Section = {
  image: string;
  title: string;
  description: string;
  to: string;
};

const sections: Section[] = [
  {
    image: 'assets/math.png',
    title: 'Mathematics',
    description:
      'Calculus, linear algebra, engineering math, probability, statistics, discrete math, numerical analysis, graph theory.',
    to: '/math',
  },
  {
    image: 'assets/cs.png',
    title: 'Computer Science',
    description:
      'Algorithms, data structures, programming languages, OS, databases, computer architecture, NLP, cryptography, software engineering.',
    to: '/cs',
  },
  {
    image: 'assets/physics.png',
    title: 'Physics',
    description:
      'General physics, mechanics, signals & systems, quantum mechanics, quantum field theory, simulation of dynamical systems.',
    to: '/physics',
  },
  {
    image: 'assets/chemistry.png',
    title: 'Chemistry',
    description:
      'General chemistry — atoms, bonds, reactions, thermodynamics, kinetics, and basic organic chemistry.',
    to: '/chemistry',
  },
  {
    image: 'assets/quantum-computing.png',
    title: 'Quantum Information Science',
    description:
      'Quantum computing, communication, internet, sensing, and security — qubits, QKD, teleportation, quantum repeaters, PQC.',
    to: '/quantum-information-science',
  },
];

function HomepageSections() {
  return (
    <section className={styles.sections}>
      <div className="container">
        <div className="row">
          {sections.map((section) => (
            <div key={section.title} className={clsx('col col--6', styles.col)}>
              <Link to={section.to} className={styles.sectionCard}>
                <img
                  src={section.image}
                  alt={`${section.title} logo`}
                  className={styles.sectionImage}
                />
                <Heading as="h2">{section.title}</Heading>
                <p>{section.description}</p>
                <span className={styles.sectionCta}>Browse →</span>
              </Link>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

export default function Home(): ReactNode {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={siteConfig.title}
      description="Personal notes on mathematics, computer science, physics and chemistry.">
      <HomepageHeader />
      <main>
        <HomepageSections />
      </main>
    </Layout>
  );
}
