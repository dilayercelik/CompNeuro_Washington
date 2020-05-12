% Quiz 3 answer to Question 1

% Create symbolic variable x
syms x

% normal probability density function 1 and 2
y1 = normpdf(x, 5, 0.5)
y2 = normpdf(x, 7, 1)

% solve the equation y1 = y2 (intersection) for x
answer_x = solve(2 * y1 == y2, x)

% variable precision arithmetic
vpa(answer_x)


% Answer = 5.978 i.e. 2nd value of answer_x
% because we need to choose the value in the middle of the two normal
% distributions (see course notes for a refresher)

