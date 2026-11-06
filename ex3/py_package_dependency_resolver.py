
def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    result = []
    pending = sorted(packages)

    while pending:
        ready = []

        for pkg in pending:
            if all(dep not in packages or dep in result for dep in packages[pkg]):
                ready.append(pkg)

        if not ready:
            return []

        for pkg in ready:
            result.append(pkg)
            pending.remove(pkg)

    return result
