extern crate day8_seven_segment_search;
use day8_seven_segment_search as day;
use criterion::{criterion_group, criterion_main, Criterion};

fn ben(c: &mut Criterion) {
    c.bench_function("day8", |b| b.iter(|| day::solve_p()));
}

criterion_group!(benches, ben);
criterion_main!(benches);
