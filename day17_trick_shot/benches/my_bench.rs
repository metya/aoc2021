extern crate day17_trick_shot;
use day17_trick_shot as day17;
use criterion::{criterion_group, criterion_main, Criterion};

fn ben(c: &mut Criterion) {
    c.bench_function("day17", |b| b.iter(|| day17::main()));
}

criterion_group!(benches, ben);
criterion_main!(benches);
