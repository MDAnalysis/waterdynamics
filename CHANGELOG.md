# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

<!--
The rules for this file:
  * entries are sorted newest-first.
  * summarize sets of changes - don't reproduce every git log comment here.
  * don't ever delete anything.
  * keep the format consistent:
    * do not use tabs but use spaces for formatting
    * 79 char width
    * YYYY-MM-DD date format (following ISO 8601)
  * accompany each entry with github issue/PR number (Issue #xyz)
-->

## [1.1.0] - 2024-01-11

### Authors
- ianmkenney
- IAlibay

### Added
- Support for Python 3.12 (PR #28)

### Fixed
- Removed import of analysis.hbonds and associated import warning (PR #28)

### Changed
- reorganized Sphinx docs (PR #26)
- switch from versioneer to versioningit (PR #28)

### Removed

## [1.0.0] - 2023-10-18

### Authors
- ianmkenney
- orbeckst

### Fixed
- package deployment workflow enforces correct options regarding tests
- formatting fixes in AUTHORS.md (PR #12)

## [0.1.0] - 2023-10-13

The original `MDAnalysis.analysis.waterdynamics` was written by Alejandro 
Bernardin in 2015 and had been part of MDAnalysis since release 0.11.0,
https://docs.mdanalysis.org/2.6.1/documentation_pages/analysis/waterdynamics.html.
Ian Kenney created the `waterdynamics` MDAKit in 2023, based on the original
code in MDAnalysis. Additional contributors to the original source code are 
listed in the AUTHORS.md file.

### Authors
- ianmkenney

### Added
- the core functionality of waterdynamics (and its tests) was implemented
  using the source code from MDAnalysis.analysis.waterdynamics (#3)
- documentation deployed to github pages and read the docs (PR #5 #6)

[Unreleased]: https://github.com/MDAnalysis/waterdynamics/compare/1.0.0...HEAD
[1.0.0]: https://github.com/MDAnaylsis/waterdynamics/compare/0.1.0...1.0.0
[0.1.0]: https://github.com/MDAnalysis/waterdynamics/releases/tag/0.1.0
