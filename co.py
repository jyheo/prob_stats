import thinkstats.correlation as co

print 'Covariance Test:'

xs = [1, 3, 5, 6, 7]
ys = [10, 30, 60, 70, 80]
zs = [7, 6, 5, 3, 1]
ns = [3, 2, 1, 2, 3]

print co.Cov(xs, ys)
print co.Cov(xs, zs)
print co.Cov(xs, ns)

print 'Correlation Test:'

print co.Corr(xs, ys)
print co.Corr(xs, zs)
print co.Corr(xs, ns)


print 'Spearman Correlation Test:'

print co.SpearmanCorr(xs, ys)
print co.SpearmanCorr(xs, zs)
print co.SpearmanCorr(xs, ns)

print 'Linear Least Squares Test:'

print co.LeastSquares(xs, ys)
print co.LeastSquares(xs, zs)
print co.LeastSquares(xs, ns)


print 'R^2'
inter, slope = co.LeastSquares(xs, ys)
res = co.Residuals(xs, ys, inter, slope)
print co.CoefDetermination(ys, res)

inter, slope = co.LeastSquares(xs, zs)
res = co.Residuals(xs, zs, inter, slope)
print co.CoefDetermination(zs, res)

inter, slope = co.LeastSquares(xs, ns)
res = co.Residuals(xs, ns, inter, slope)
print co.CoefDetermination(ns, res)
