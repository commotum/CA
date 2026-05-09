Yes. The simple version is:

```text
Each neighborhood component becomes one rule-input channel.

For each channel:
    n_i + channel_rule_type_i -> S_i

Then:
    S = S1 · S2 · ... · Sm
    R = a^S
```

So your Dyadaxes example is exactly:

```text
a = 2

n1 = 1
n2 = 4
n3 = 4

n1_rtype = EXHAUSTIVE
n2_rtype = THRESHOLDED_TOTALISTIC
n3_rtype = THRESHOLDED_TOTALISTIC

S1 = 2
S2 = 2
S3 = 2

S = 2 · 2 · 2 = 8
R = 2^8 = 256
```

The only adjustment I’d make is naming: plain `TOTALISTIC` gives the full count, so for `n = 4` it would have `5` states:

```text
count ∈ {0,1,2,3,4}
S = n + 1 = 5
```

But Dyadaxes does not keep all 5 count states. It splits the count into a binary threshold state:

```text
aggregate = active_count >= threshold
```

So I’d call that:

```text
THRESHOLDED_TOTALISTIC
```

or:

```text
TOTALISTIC_SPLIT
```

## Minimal API

```ts
type ChannelRuleType =
  | "EXHAUSTIVE"
  | "TOTALISTIC"
  | "THRESHOLDED_TOTALISTIC"
  | "HISTOGRAM_TOTALISTIC"
  | "SUM_TOTALISTIC";

type RuleChannel = {
  id: string;
  n: number;
  ruleType: ChannelRuleType;
  threshold?: number;
};

type RuleFamily = {
  alphabetSize: number; // a
  channels: RuleChannel[];
};
```

## Minimal counting functions

```ts
function channelStateCount(a: number, channel: RuleChannel): bigint {
  const n = BigInt(channel.n);
  const A = BigInt(a);

  switch (channel.ruleType) {
    case "EXHAUSTIVE":
      return A ** n;

    case "TOTALISTIC":
      // binary active-count totalistic
      return n + 1n;

    case "THRESHOLDED_TOTALISTIC":
      // count is collapsed to false/true
      return 2n;

    case "SUM_TOTALISTIC":
      // assumes values are 0...(a-1)
      return n * BigInt(a - 1) + 1n;

    case "HISTOGRAM_TOTALISTIC":
      return choose(n + A - 1n, A - 1n);
  }
}

function inputStateCount(family: RuleFamily): bigint {
  const a = family.alphabetSize;

  return family.channels.reduce(
    (product, channel) => product * channelStateCount(a, channel),
    1n
  );
}

function ruleCount(family: RuleFamily): bigint {
  const a = BigInt(family.alphabetSize);
  const S = inputStateCount(family);

  return a ** S;
}
```

## Dyadaxes as the API object

```ts
const dyadaxes2D: RuleFamily = {
  alphabetSize: 2,
  channels: [
    {
      id: "s",
      n: 1,
      ruleType: "EXHAUSTIVE",
    },
    {
      id: "a",
      n: 4,
      ruleType: "THRESHOLDED_TOTALISTIC",
      threshold: 2,
    },
    {
      id: "o",
      n: 4,
      ruleType: "THRESHOLDED_TOTALISTIC",
      threshold: 2,
    },
  ],
};
```

Counts:

```text
S1 = 2^1 = 2
S2 = 2
S3 = 2

S = 2 · 2 · 2 = 8
R = 2^8 = 256
```

## Channel-state formulas

```text
EXHAUSTIVE:
    S_i = a^n_i

BINARY TOTALISTIC:
    S_i = n_i + 1

THRESHOLDED_TOTALISTIC:
    S_i = 2

SUM_TOTALISTIC:
    S_i = n_i(a - 1) + 1

HISTOGRAM_TOTALISTIC:
    S_i = C(n_i + a - 1, a - 1)
```

Then always:

```text
S = Π S_i
R = a^S
```

## Dyadaxes index

Since each channel has `S_i = 2`, the channel values are binary:

```text
s ∈ {0,1}
p ∈ {0,1}
q ∈ {0,1}
```

Then:

```text
index = 4*s + 2*p + q
next = (rule_id >> index) & 1
```

So the simplified framing is:

```text
component neighborhood -> component rule-type -> S_i
compose components -> S
rule table size -> R
```

For Dyadaxes, the global rule is exhaustive over the three compressed channel states, not exhaustive over all raw cells.
