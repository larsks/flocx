# FLOCX matching syntax

A Bid submitted to the FLOCX Marketplace service may specify a set of criteria
that must be satisfied in order to match with an available Offer. This document
describes the syntax used to specify these matching rules in the REST API.

## Basic syntax

A match expression consists of a list of 3-tuples `[expression, operator,
value]`, where:

- `expression` is a [JMESPath][] expression used to extract a value from the
  node metadata,

- `operator` is one of the operators described in this document, and

- `value` is the value against which the expression is compared.

When there are multiple 3-tuples in a match expression, they are combined using
a logical `AND` operation (i.e., they all must match).

[jmespath]: http://jmespath.org/specification.html

## Operators

Prefix an operator with `!` to negate the comparison.

### Null operator

If `operator` is `null`, the value of `expression` is interpreted in a boolean
context (and `value` is ignored).

### Numeric operators

- `==` - equals
- `!=` - does not equal
- `>` - greater than
- `<` - less than
- `>=` - greater than or equal to
- `<=` - less than or equal to

### String Operators

- `eq` - equals
- `ne` - does not equal
- `startswith` - string starts with the given value
- `endswith` - string ends with the given value
- `matches` - string matches a regular expression

### List operators

- `in` - string is contained in the given list
- `contains` - list contains the given string

## Examples

Match a specific host architecture:

```json
[
  ["cpu_arch", "eq", "x86_64"]
]
```

Match a host with at least 48GB memory:

```json
[
  ["memory_mb", ">=", 48000]
]
```

Match a host with at least 16 x86_64 CPUs:

```json
[
  ["cpu_arch", "eq", "x86_64"],
  ["inventory.cpu.count", ">=", 16]
]
```

Match a host that supports hardware-accelerated virtualization:

```json
[
  [ "inventory.cpu.flags", "contains", "vmx"]
]
```

Match a host that **does not** support hardware-accelerated virtualization:

```json
[
  [ "inventory.cpu.flags", "!contains", "vmx"]
]
```

Match a host with a least two rotational hard disks:

```json
[
  ["length(inventory.disks[?\"rotational\" == `true`])", ">=", 2]
]
```

Match a host with 1 or more rotational hard disks:

```json
[
  ["inventory.disks[?\"rotational\"==`true`]", null, null]
]
```

Match a specific manufacturer and product:

```json
[
  ["inventory.system_vendor.manufacturer", "matches", "Dell"],
  ["inventory.system_vendor.product_name", "matches", "PowerEdge M620"]
]
```
