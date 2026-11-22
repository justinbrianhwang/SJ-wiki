import type {ReactNode} from 'react';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';

import styles from './index.module.css';

const sections = [
  {
    title: 'Mathematics',
    to: '/math',
    description:
      'Calculus, linear algebra, engineering math, probability, statistics, discrete math, numerical analysis, graph theory.',
  },
  {
    title: 'Computer Science',
    to: '/cs',
    description:
      'Algorithms, data structures, programming languages, OS, databases, architecture, ML, NLP, cryptography, software engineering.',
  },
  {
    title: 'Physics',
    to: '/physics',
    description:
      'General physics, mechanics, signals & systems, quantum mechanics, quantum field theory, dynamical systems.',
  },
  {
    title: 'Chemistry',
    to: '/chemistry',
    description:
      'General chemistry: atoms, bonds, reactions, thermodynamics, kinetics, basic organic chemistry.',
  },
  {
    title: 'Quantum Information Science',
    to: '/quantum-information-science',
    description:
      'Quantum computing, communication, sensing, and security: qubits, QKD, teleportation, repeaters, PQC.',
  },
];

export default function Home(): ReactNode {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={siteConfig.title}
      description="Personal notes on mathematics, computer science, physics and chemistry.">
      <div className={styles.page}>
        <aside className={styles.side}>
          <div className={styles.brand}>
            <img src="img/logo.png" alt="" className={styles.brandLogo} />
            <span>SJ Wiki</span>
          </div>
          <div className={styles.meta}>Library</div>
          <ul>
            {sections.map((s) => (
              <li key={s.to}>
                <Link to={s.to}>{s.title}</Link>
              </li>
            ))}
          </ul>
        </aside>
        <main>
          <div className={styles.meta}>Personal knowledge base</div>
          <Heading as="h1" className={styles.title}>
            Sunjun Hwang&apos;s Wiki
          </Heading>
          <p className={styles.lede}>
            Notes I keep while studying mathematics, computer science, physics
            and chemistry, plus reading notes on papers.
          </p>
          <Heading as="h2" className={styles.h2}>
            Explore the library
          </Heading>
          <ol className={styles.index}>
            {sections.map((s, i) => (
              <li key={s.to}>
                <span className={styles.num}>{String(i + 1).padStart(2, '0')}</span>
                <Link to={s.to} className={styles.row}>
                  <span className={styles.name}>{s.title}</span>
                  <span className={styles.desc}>{s.description}</span>
                  <span className={styles.arrow} aria-hidden="true">↗</span>
                </Link>
              </li>
            ))}
          </ol>
        </main>
      </div>
    </Layout>
  );
}
