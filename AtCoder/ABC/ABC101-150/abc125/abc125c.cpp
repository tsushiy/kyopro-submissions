#include <bits/stdc++.h>
using namespace std;
#define REP(i,b,e) for(int i=(b);i<(e);++i)
#define RREP(i,b,e) for(int i=(b)-1;i>=e;--i)
#define rep(i,e) for(int i=0;i<(e);++i)

inline void print(void) { cout<<'\n'; }
template<class T> inline void print(const T &x) { cout<<x<<'\n'; }
template<class T, class... U> inline void print(const T &x, const U&... y) { cout<<x<<" "; print(y...); }

template<typename T>
T gcd(T a, T b) {
  while (a) {
    b %= a;
    swap(a, b);
  }
  return b;
}

int main() {
  int n; cin>>n;
  vector<int> a(n);
  rep(i, n) cin>>a[i];

  vector<int> l(n), r(n);
  l[0] = a[0];
  r[n-1] = a[n-1];
  REP(i, 1, n) l[i] = gcd(l[i-1], a[i]);
  RREP(i, n-1, 0) r[i] = gcd(r[i+1], a[i]);
  int ans = max(l[n-2], r[1]);
  REP(i, 1, n-1) ans = max(ans, gcd(l[i-1], r[i+1]));
  print(ans);
  return 0;
}